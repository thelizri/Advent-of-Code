import re

def loopRange(first, second):
	(x1, y1) = first
	(x2, y2) = second

	if x1 == x2:
		if y2 < y1: y1, y2 = y2, y1
		for y in range(y1, y2+1):
			updateMap(x1, y)

	elif y1 == y2:
		if x2 < x1: x1, x2 = x2, x1
		for x in range(x1, x2+1):
			updateMap(x, y1)

def updateMap(x, y):
	sum = dict.get((x, y))
	if sum == None:
		dict.update({(x, y): 1})
	else: 
		dict.update({(x, y): 1+sum})

file = open("day5.txt")
dict = {}

for row in file:
	x1, y1, x2, y2 = re.findall("\d+", row)
	x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
	loopRange((x1, y1), (x2, y2))
	
result = list(filter(lambda x: x > 1, dict.values()))
print(len(result))
