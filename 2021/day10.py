# stack, uses pop()
# queue, uses pop(0)
file = open("day10.txt", "r")
file.seek(0)
text_list = [row.strip() for row in file.readlines()]
file.close()

# ): 3 points.
# ]: 57 points.
# }: 1197 points.
# >: 25137 points.

def isOpening(char):
	return char in "{([<"
def isClosing(char):
	return char in ")]}>"
def isMatch(charOpen, charClose):
	if charOpen == "{":
		return charClose == "}"
	elif charOpen == "[":
		return charClose == "]"
	elif charOpen == "(":
		return charClose == ")"
	elif charOpen == "<":
		return charClose == ">"
	return None

score = {")": 3, "]": 57, "}": 1197, ">": 25137}

points = 0
stack = []
for row in text_list:
	for char in row:
		if isOpening(char): stack.append(char)
		else:
			res = isMatch(stack.pop(), char)
			if not res:
				points += score.get(char)
				break;
	stack.clear()

print("Part 1: "+str(points))