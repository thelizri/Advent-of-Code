hex_to_bin = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}

score = 0
length = 0

def getBinary(string):
    result = ''
    for s in string:
        result += hex_to_bin[s]
    return result

def convertToNumber(string):
    return int(string, base=2)

def getVersion(string):
    packet_version = string[0:3]
    type_id = string[3:6]
    length_id = string[6]
    rest = string[6:]

    global score, length
    length += 1
    score += convertToNumber(packet_version)

    if type_id == '100':
        while rest[0] != '0':
            rest = rest[5:]
        rest = rest[5:]
        return rest
    elif length_id == '0':
        return string[22:]
    else:
        return string[18:]

file = open("day16.txt", "r")
my_input = file.readline().strip()
file.close()
string = getBinary(my_input)

while len(string) > 6:
    string = getVersion(string)

print(f"Part 1: {score}")

#Part 2
scores = []
themap = dict()
pos = 0

for i in range(length):
    scores.append(0)

def getValueLiteral(string):
    global pos
    score = ''
    rest = string[6:]; pos+=6
    while rest[0] != '0':
        score += rest[1:5]
        rest = rest[5:]; pos+=5
    score += rest[1:5]
    rest = rest[5:]; pos+=5
    return (convertToNumber(score), rest)

def evaluate_packet(packet, i):
    global pos
    current = pos
    type_id = packet[3:6]
    length_id = packet[6]

    if type_id == '100':
        (score, rest) = getValueLiteral(packet)
        scores[i] = score
        themap[i] = (current, pos)
        return rest
    elif length_id == '0':
        pos += 22
        themap[i] = (current, pos)
        return packet[22:]
    else:
        pos += 18
        themap[i] = (current, pos)
        return packet[18:]

def checkrange(r1, r2):
    return set((r1)).issubset(r2)

def product(li):
    result = 1
    for i in li:
        result *= i
    return result

def evaluate(packet, number, start, end):
    type_id = packet[3:6]
    length_id = packet[6]
    if type_id == '100':
        return None

    packet_scores = []

    if length_id == '0':
        lengthbits = convertToNumber(packet[7:22])
        packetstocheck = []
        r2 = range(end, end+lengthbits)
        for item in themap.items():
            (key, (r1_start, r1_end)) = item
            r1 = range(r1_start, r1_end)
            if checkrange(r1, r2):
                packetstocheck.append(key)
        for i in packetstocheck:
            packet_scores.append(scores[i])
    else:
        many = convertToNumber(packet[7:18])
        for i in range(x+1, x+1+many):
            packet_scores.append(scores[i])

    if type_id == '000':
        scores[number] = sum(packet_scores)
    elif type_id == '001':
        scores[number] = product(packet_scores)
    elif type_id == '010':
        scores[number] = min(packet_scores)
    elif type_id == '011':
        scores[number] = max(packet_scores)
    elif type_id == '101':
        if packet_scores[0] > packet_scores[1]:
            scores[number] = 1
        else:
            scores[number] = 0
    elif type_id == '110':
        if packet_scores[0] < packet_scores[1]:
            scores[number] = 1
        else:
            scores[number] = 0
    elif type_id == '111':
        if packet_scores[0] == packet_scores[1]:
            scores[number] = 1
        else:
            scores[number] = 0



# If the length type ID is 0, then the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
# If the length type ID is 1, then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.


string = getBinary(my_input)
i = 0
while len(string) > 6:
    string = evaluate_packet(string, i)
    i+=1

string = getBinary(my_input)
for x in range(length-1, -1, -1):
    (start, end) = themap[x]
    packet = string[start:end]
    evaluate(packet, x, start, end)
print(scores)


# Packets with type ID 0 are sum packets - their value is the sum of the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
# Packets with type ID 1 are product packets - their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
# Packets with type ID 2 are minimum packets - their value is the minimum of the values of their sub-packets.
# Packets with type ID 3 are maximum packets - their value is the maximum of the values of their sub-packets.
# Packets with type ID 5 are greater than packets - their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
# Packets with type ID 6 are less than packets - their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
# Packets with type ID 7 are equal to packets - their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
