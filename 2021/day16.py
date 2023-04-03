from operator import add, mul, gt, lt, eq
ops = (add, mul, lambda *x: min(x), lambda *x: max(x), None, gt, lt, eq)

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

def getVersion(string, score, length):
    packet_version = string[0:3]
    type_id = string[3:6]
    length_id = string[6]
    rest = string[6:]

    length += 1
    score += int(packet_version, 2)

    if type_id == '100':
        (rest, value) = evaluate_literal(rest)
        return (rest, score, length)
    elif length_id == '0':
        return (string[22:], score, length)
    else:
        return (string[18:], score, length)

def evaluate_literal(packet):
    answer = ""
    while packet[0] != '0':
        answer += packet[1:5]
        packet = packet[5:]
    answer += packet[1:5]
    packet = packet[5:]
    return (packet, int(answer, 2))

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


# If the length type ID is 0, then the next 15 bits are a number that represents the total length in bits of the sub-packets contained by this packet.
# If the length type ID is 1, then the next 11 bits are a number that represents the number of sub-packets immediately contained by this packet.

# Packets with type ID 0 are sum packets - their value is the sum of the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
# Packets with type ID 1 are product packets - their value is the result of multiplying together the values of their sub-packets. If they only have a single sub-packet, their value is the value of the sub-packet.
# Packets with type ID 2 are minimum packets - their value is the minimum of the values of their sub-packets.
# Packets with type ID 3 are maximum packets - their value is the maximum of the values of their sub-packets.
# Packets with type ID 5 are greater than packets - their value is 1 if the value of the first sub-packet is greater than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
# Packets with type ID 6 are less than packets - their value is 1 if the value of the first sub-packet is less than the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
# Packets with type ID 7 are equal to packets - their value is 1 if the value of the first sub-packet is equal to the value of the second sub-packet; otherwise, their value is 0. These packets always have exactly two sub-packets.
