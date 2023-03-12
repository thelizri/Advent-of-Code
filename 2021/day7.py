import re

def calcMoves(li, pos):
	totalMoves = 0
	for x in li:
		totalMoves += abs(x-pos)
	return totalMoves

#1+2+3+...+n=n(n+1)/2 
def calcFuelPart2(li, pos):
	totalMoves = 0
	for x in li:
		n = abs(x-pos)
		totalMoves += n*(n+1)/2
	return int(totalMoves)

mylist = []
file = open("day7.txt")
for row in file:
	numbers = re.findall("\d+", row)
	numbers = map(lambda x: int(x), numbers)
	mylist.extend(numbers)

part1 = []
part2 = []
small = min(mylist)
large = max(mylist)+1
for num in range(small, large):
	part1.append(calcMoves(mylist, num))
	part2.append(calcFuelPart2(mylist, num))


print("Part 1: "+str(min(part1)))
print("Part 2: "+str(min(part2)))

file.close()