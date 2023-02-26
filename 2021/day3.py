#Part 1
file = open("day3.txt", "r")
mylist = []
length = 1
firstrow = file.readline()
for letter in firstrow:
	if(letter == "1"):
		mylist.append(1)
	elif(letter == "0"): 
		mylist.append(0)

for row in file:
	length += 1
	for i in range(len(mylist)):
		if(row[i] == "1"):
			mylist[i] += 1
file.close()
gamma = ""
epsilon = ""
for n in mylist:
	if int(n) > length/2:
		gamma += "1"
		epsilon += "0"
	else:
		gamma += "0"
		epsilon += "1"

result = int(epsilon, 2)*int(gamma, 2)
print("Part 1: "+str(result))

#Part 2
def getRows():
	file = open("day3.txt", "r")
	result = []
	for row in file:
		result.append(row.replace("\n", ""))
	file.close()
	return result

def getMostCommon(file, pos, default):
	num1 = 0
	num0 = 0
	for row in file:
		if row[pos] == "1":
			num1 += 1
		else:
			num0 += 1
	if num1 > num0:
		return "1"
	elif num1 == num0:
		return default
	else:
		return "0"

def getLeastCommon(file, pos, default):
	num1 = 0
	num0 = 0
	for row in file:
		if row[pos] == "1":
			num1 += 1
		else:
			num0 += 1
	if num1 < num0:
		return "1"
	elif num1 == num0:
		return default
	else:
		return "0"


#mylist = list(filter(lambda x: x[0]==common, mylist))
mylist = getRows()
length = len(mylist[0])
pos = 0
while len(mylist) > 1:
	common = getMostCommon(mylist, pos, "1")
	mylist = list(filter(lambda x: x[pos]==common, mylist))
	pos += 1
oxygen = int(mylist[0], 2)

mylist = getRows()
length = len(mylist[0])
pos = 0
while len(mylist) > 1:
	common = getLeastCommon(mylist, pos, "0")
	mylist = list(filter(lambda x: x[pos]==common, mylist))
	pos += 1
co2rating = int(mylist[0], 2)

result = oxygen*co2rating
print("Part 2: "+str(result))
