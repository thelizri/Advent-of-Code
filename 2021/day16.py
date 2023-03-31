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

def getHeader(string):
	packet_version = string[0:3]
	type_id = string[3:6]
	rest = string[6:]

	if type_id == '100':
		while rest[0] != '0':
			rest = rest[5:]
		rest = rest[5:]
	return rest


test = "D2FE28"
string = getBinary(test)
string = getHeader(string)
print(string)



