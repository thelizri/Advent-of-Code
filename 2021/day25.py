#Reading input
file = open("day25.txt", "r")
file.seek(0)

matrix = []
for row in file:
	line = []
	for character in row.strip():
		if character == ">":
			line.append(1)
		elif character == "v":
			line.append(-1)
		else: line.append(0)
	matrix.append(line)

height = len(matrix)
width = len(matrix[0])

#Part 1
#1 represents rightwards direction
#-1 represents downwards direction
#First we move right
#Then we move down

def move(x, y, direction):
	if direction==1:
		x = (x+1)%width
	elif direction == -1:
		y = (y+1)%height
	return (x,y)

def goRight():
	li = []
	for y in range(height):
		for x in range(width):
			if matrix[y][x] == 1:
				(nX, nY) = move(x, y, 1)
				if matrix[nY][nX]==0:
					li.append((x,y))
	for x,y in li:
		matrix[y][x] = 0
		(nX, nY) = move(x, y, 1)
		matrix[nY][nX] = 1

	return len(li)

def goDown():
	li = []
	for y in range(height):
		for x in range(width):
			if matrix[y][x] == -1:
				(nX, nY) = move(x, y, -1)
				if matrix[nY][nX]==0:
					li.append((x,y))
	for x,y in li:
		matrix[y][x] = 0
		(nX, nY) = move(x, y, -1)
		matrix[nY][nX] = -1

	return len(li)

def step():
	s1 = goRight()
	s2 = goDown()
	return s1 + s2

totalSteps = 1
count = 0

while totalSteps > 0:
	count += 1
	totalSteps = step()

print(f"Part 1: {count}")