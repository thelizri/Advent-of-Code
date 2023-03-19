import re

file = open("day13.txt", "r")
file.seek(0)

li = []
#Read coordinates into a tuple
for row in file:
	if row.strip() == "": break
	[x, y] = row.strip().split(",")
	li.append((x,y))

#Read instructions
instr = []
for row in file:
	[foldDir, number]=re.search(r"[xy]=\d+", row).group().split("=")
	instr.append((foldDir, int(number)))


print(li)
print(instr)