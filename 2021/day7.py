import re

def calcMoves(li, pos):
	totalMoves = 0
	for x in li:
		totalMoves += abs(x-pos)
	return totalMoves

mylist = []
file = open("day7.txt")
for row in file:
	numbers = re.findall("\d+", row)
	numbers = map(lambda x: int(x), numbers)
	mylist.extend(numbers)

result = []
small = min(mylist)
large = max(mylist)+1
for num in range(small, large):
	result.append(calcMoves(mylist, num))

print(min(result))

