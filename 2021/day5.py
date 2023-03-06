import re
file = open("day5.txt")
for row in file:
	print(re.search("\d", row))