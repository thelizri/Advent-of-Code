import re

def diagonalStep(first, second):
	(x1, y1) = first
	(x2, y2) = second
	if x1 < x2: x1 += 1
	else: x1 -= 1
	if y1 < y2: y1 += 1
	else: y1 -= 1
	return (x1, y1)

def loopRange(first, second):
	(x1, y1) = first
	(x2, y2) = second

	if x1 == x2:
		if y2 < y1: y1, y2 = y2, y1
		for y in range(y1, y2+1):
			updateMap(x1, y, map1)
			updateMap(x1, y, map2)

	elif y1 == y2:
		if x2 < x1: x1, x2 = x2, x1
		for x in range(x1, x2+1):
			updateMap(x, y1, map1)
			updateMap(x, y1, map2)
	else:
		while first != second:
			(x, y) = first
			updateMap(x,y, map2)
			first = diagonalStep(first, second)
		(x, y) = second	
		updateMap(x,y, map2)

def updateMap(x, y, themap):
	sum = themap.get((x, y))
	if sum == None:
		themap.update({(x, y): 1})
	else: 
		themap.update({(x, y): 1+sum})

file = open("day5.txt")
map1 = {}
map2 = {}

for row in file:
	x1, y1, x2, y2 = re.findall("\d+", row)
	x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
	loopRange((x1, y1), (x2, y2))

result = list(filter(lambda x: x > 1, map1.values()))
print("Part 1: "+str(len(result)))

result = list(filter(lambda x: x > 1, map2.values()))
print("Part 2: "+str(len(result)))

file.close()