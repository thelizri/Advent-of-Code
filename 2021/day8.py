import re

def test(s):
	if len(s) > 1 and len(s) < 5: return True
	elif len(s) == 7: return True
	else: return False

file = open("day8.txt", "r")
file.seek(0)

sum = 0
for row in file:
	li = row.split("|")
	codes = re.findall("[a-z]+", li[1])
	matches = list(filter(test, codes))
	sum += len(matches)

print("Part 1: "+str(sum))