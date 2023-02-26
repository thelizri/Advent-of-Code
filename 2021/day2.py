#Part 1
x = 0
y = 0
file = open("day2.txt", "r")
for row in file:
	[instruction, value] = row.split()
	if(instruction == "forward"):
		x += int(value)
	elif(instruction == "up"):
		y -= int(value)
	else:
		y += int(value)
result = x*y
print("Part 1: "+str(result))

#Part 2
x = 0
y = 0
aim = 0
file = open("day2.txt", "r")
for row in file:
	[instruction, value] = row.split()
	if(instruction == "forward"):
		x += int(value)
		y += aim*int(value)
	elif(instruction == "up"):
		aim -= int(value)
	else:
		aim += int(value)
result = x*y
print("Part 2: "+str(result))