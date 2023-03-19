import re

file = open("day13.txt", "r")
file.seek(0)

li = []
#Read coordinates into a tuple
for row in file:
	if row.strip() == "": break
	[x, y] = row.strip().split(",")
	li.append((int(x),int(y)))

#Read instructions
instr = []
for row in file:
	[foldDir, number]=re.search(r"[xy]=\d+", row).group().split("=")
	instr.append((foldDir, int(number)))

def foldX(li, X):
	pretransform = list(filter(lambda xy: xy[0]>X, li))
	li = list(filter(lambda xy: xy[0]<X, li))
	# X-(x-X) = 2X-x
	flipped = list(map(lambda xy: (2*X-xy[0], xy[1]), pretransform))
	li.extend(flipped)
	return li

def foldY(li, Y):
	pretransform = list(filter(lambda xy: xy[1]>Y, li))
	li = list(filter(lambda xy: xy[1]<Y, li))
	# Y-(y-Y) = 2Y-y
	flipped = list(map(lambda xy: (xy[0], 2*Y-xy[1]), pretransform))
	li.extend(flipped)
	return li

def fold(instruction, li):
	(foldDir, number) = instruction
	if foldDir == "x":
		return foldX(li, number)
	elif foldDir == "y":
		return foldY(li, number)
	else:
		print("Error")

li = fold(instr[0], li)
points = set(())
for t in li:
	points.add(t)

part1_answer = str(len(points))
print("Part 1: "+part1_answer)

#Part 2
for index in range(1, len(instr)):
	li = fold(instr[index], li)
points = set(())
for t in li:
	points.add(t)

maxX = max(points, key=lambda k: k[0])[0] + 1
maxY = max(points, key=lambda k: k[1])[1] + 1

#Will output the characters that are the answer for part 2
for y in range(maxY):
	for x in range(maxX):
		t = (x,y)
		if t in points: print("#", end="")
		else: print(".", end="")
	print(" ")