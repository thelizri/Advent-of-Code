hex_to_bin = {
'0': '0000','1': '0001','2': '0010','3': '0011',
'4': '0100','5': '0101','6': '0110','7': '0111',
'8': '1000','9': '1001','A': '1010','B': '1011',
'C': '1100','D': '1101','E': '1110','F': '1111'
}

def getBinary(string):
    result = ''
    for s in string:
        result += hex_to_bin[s]
    return result

def convertToNumber(string):
    return int(string, base=2)

def getVersion(string, score, length):
    packet_version = string[0:3]
    type_id = string[3:6]
    length_id = string[6]
    rest = string[6:]

    length += 1
    score += convertToNumber(packet_version)

    if type_id == '100':
        while rest[0] != '0':
            rest = rest[5:]
        rest = rest[5:]
        return (rest, score, length)
    elif length_id == '0':
        return (string[22:], score, length)
    else:
        return (string[18:], score, length)

#Read input
file = open("day16.txt", "r")
my_input = file.readline().strip()
string = getBinary(my_input)
file.close()

#Part 1
score = 0
length = 0
while len(string) > 6:
    (string, score, length) = getVersion(string, score, length)

print(f"Part 1: {score}")

###########################################################################################
#Part 2

def createPackets(packets, binary, pos):
    current = pos
    type_id = binary[(pos+3):(pos+6)]
    length_id = binary[(pos+6)]

    if type_id == '100':
        (score, rest, pos) = getValueLiteral(binary[pos:], pos)
        packets.append(binary[current:pos])
        return pos
    elif length_id == '0':
        pos += 22
        packet = binary[current:pos]
        if pos-current == len(packet): 
            packets.append(binary[current:pos])
        return pos
    else:
        pos += 18
        packet = binary[current:pos]
        if pos-current == len(packet): 
            packets.append(binary[current:pos])
        return pos

def getValueLiteral(string, pos):
    score = ''
    rest = string[6:]; pos+=6
    while rest[0] != '0':
        score += rest[1:5]
        rest = rest[5:]; pos+=5
    score += rest[1:5]
    rest = rest[5:]; pos+=5
    return (convertToNumber(score), rest, pos)

def checkrange(r1, r2):
    return set((r1)).issubset(r2)

def op_code(packet_scores, number, type_id):
    if type_id == '000':
        scores[number] = sum(packet_scores)
    elif type_id == '001':
        product = 1
        for i in packet_scores: product *= i
        scores[number] = product
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

def eval_packet(packets, number, scores, owned):
    packet = packets[number]
    type_id = packet[3:6]
    length_id = packet[6]
    owned[number] = False

    if type_id == '100':
        (score, rest, pos) = getValueLiteral(packet, 0)
        scores[number] = score
        return None

    packet_numbers = []

    if length_id == '0':
        bits = convertToNumber(packet[7:22])
        for i in range(number+1, len(packets)):
            if bits <= 0: break
            if owned.get(i, False): continue
            if len(packets[i]) > bits: continue
            packet_numbers.append(i)
            owned[i] = True
            bits -= len(packets[i])
    else:
        amount = convertToNumber(packet[7:18])
        for i in range(number+1, len(packets)):
            if amount<=0: break
            if owned.get(i, False): continue
            packet_numbers.append(i)
            owned[i] = True
            amount -= 1

    packet_scores = []
    for i in packet_numbers:
        packet_scores.append(scores[i])

    op_code(packet_scores, number, type_id)







binary = getBinary(my_input)

pos = 0
packets = []
while pos + 6 < len(binary):
    pos = createPackets(packets, binary, pos)

print(binary)
print(packets)

owned = dict()
scores = dict()
for i in range(len(packets)-1, -1, -1):
    eval_packet(packets, i, scores, owned)

print(binary)
print(packets)
print(scores)

# If the length type ID is 0, then the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
# If the length type ID is 1, then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.

# Packets with type ID 0 are sum packets - their value is the sum of the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
# Packets with type ID 1 are product packets - their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
# Packets with type ID 2 are minimum packets - their value is the minimum of the values of their sub-packets.
# Packets with type ID 3 are maximum packets - their value is the maximum of the values of their sub-packets.
# Packets with type ID 5 are greater than packets - their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
# Packets with type ID 6 are less than packets - their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
# Packets with type ID 7 are equal to packets - their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
