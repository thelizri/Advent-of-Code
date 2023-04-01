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

    global score
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
string = getBinary(my_input)

while len(string) > 6:
    string = getVersion(string)

print(f"Part 1: {score}")

#Part 2

def getValueLiteral(string):
    score = ''
    rest = string[6:]
    while rest[0] != '0':
        score += rest[1:5]
        rest = rest[5:]
    score += rest[1:5]
    return convertToNumber(score)

string = "D2FE28"
string = getBinary(string)
score = getValueLiteral(string)
print(score)
