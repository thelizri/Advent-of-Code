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
corrupted_lines = []
index = -1
for row in text_list:
	index += 1
	for char in row:
		if isOpening(char): stack.append(char)
		else:
			res = isMatch(stack.pop(), char)
			if not res:
				points += score.get(char)
				corrupted_lines.append(index)
				break;
	stack.clear()

print("Part 1: "+str(points))

#Part 2
#remove corrupted_lines
for i in range(0, len(corrupted_lines)):
	index = corrupted_lines[i] - i
	text_list.pop(index)

# ): 1 point.
# ]: 2 points.
# }: 3 points.
# >: 4 points.
score = {")": 1, "]": 2, "}": 3, ">": 4}
closer = {"(":")", "[":"]", "{":"}", "<":">"}
points = 0

def updateScore(closingChar):
	global points
	points = points*5 + score.get(closingChar)

stack = []
total_points = []
for row in text_list:
	for char in row:
		if isOpening(char): stack.append(char)
		else: stack.pop()
	stack.reverse()
	for char in stack:
		updateScore(closer.get(char))
	stack.clear()
	total_points.append(points)
	points = 0

#Get middle score
total_points.sort()
index = len(total_points)//2
answer = total_points[index]
print("Part 2: "+str(answer))