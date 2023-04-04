from operator import add, mul, gt, lt, eq
ops = (lambda *x: sum(x), lambda *x: multiply(x), lambda *x: min(x), lambda *x: max(x), None, gt, lt, eq)

def multiply(x):
    result = 1
    for i in x:
        result *= i
    return result

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

def getVersion(packet, score, pos, length):
    packet_version = string[pos:pos+3]
    type_id = string[pos+3:pos+6]
    length_id = string[pos+6]
    pos += 6

    length += 1
    score += int(packet_version, 2)

    if type_id == '100':
        (pos, value) = evaluate_literal(packet, pos)
        return (score, pos, length)
    elif length_id == '0':
        return (score, pos+16, length)
    else:
        return (score, pos+12, length)

def evaluate_literal(packet, pos):
    answer = ""
    while packet[pos] != '0':
        answer += packet[pos+1:pos+5]
        pos += 5
    answer += packet[pos+1:pos+5]
    pos += 5
    return (pos, int(answer, 2))

#Read input
file = open("day16.txt", "r")
my_input = file.readline().strip()
string = getBinary(my_input)
file.close()

#Part 1
score = 0
length = 0
pos = 0
while pos + 6 < len(string):
    (score, pos, length) = getVersion(string, score, pos, length)

print(f"Part 1: {score}")

###########################################################################################
#Part 2

def calc_score(li, type_id):
    if type_id == 0:
        return sum(li)
    elif type_id == 1:
        return multiply(li)
    elif type_id == 2:
        return min(li)
    elif type_id == 3:
        return max(li)
    elif type_id == 5:
        return gt(li[0], li[1])
    elif type_id == 6:
        return lt(li[0], li[1])
    elif type_id == 7:
        return eq(li[0], li[1])


#Return (pos, value)
def evaluate_packet(packet, pos):
    #Exit condition
    if pos + 11 > len(packet):
        return (pos, 0)

    type_id = int(string[pos+3:pos+6], 2)
    length_id = string[pos+6]
    pos += 6

    #Top Level Packet is Literal
    if type_id == 4:
        (pos, value) = evaluate_literal(packet, pos)
        return (pos, value)
    #Next 15 bits 
    elif length_id == '0':
        bits = int(packet[pos+1:pos+16], 2)
        pos += 16
        score = []
        while bits > 0 and pos < len(packet):
            (newPos, newValue) = evaluate_packet(packet, pos)
            if (newPos - pos) <= bits:
                bits -= (newPos - pos)
                score.append(newValue)
            pos = newPos
        return (pos, calc_score(score, type_id))
    else:
        number = int(packet[pos+1:pos+12], 2)
        pos += 12
        score = []
        for i in range(number):
            (pos, newValue) = evaluate_packet(packet, pos)
            score.append(newValue)
            if pos >= len(packet): break
        return (pos, calc_score(score, type_id))

answer = evaluate_packet(string, 0)[1]
print(f"Part 2: {answer}")

#Calculate the value of the outermost packet
# If the length type ID is 0, then the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
# If the length type ID is 1, then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.
