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

