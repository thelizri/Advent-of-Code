file = open("day11.txt", "r")

matrix = []
for row in file:
	line = [int(char) for char in row.strip()]
	matrix.append(line)

def validCoord(coord):
	(row, col) = coord
	if row < 0 or row > 9: return False
	elif col < 0 or col > 9: return False
	return True

def getAdjacent(row, col):
	adj = [(row, col+1), (row, col-1), (row+1, col), (row-1, col),
	(row+1, col+1), (row+1, col-1), (row-1, col+1), (row-1, col-1)]
	return list(filter(validCoord, adj))

def increment(matrix):
	for row in range(0, 10):
		for col in range(0, 10):
			matrix[row][col]+=1

# First, the energy level of each octopus increases by 1.
# Then, any octopus with an energy level greater than 9 flashes
# This increases the energy level of all adjacent octopuses by 1
count = 0

def getAllPotentialFlashers(matrix, flashed):
	flashers = []
	for row in range(0, 10):
		for col in range(0, 10):
			if matrix[row][col] > 9 and (row, col) not in flashed: flashers.append((row, col))
	return flashers

def incrementAdj(matrix, flashers):
	for (row, col) in flashers:
		for (adjRow, adjCol) in getAdjacent(row, col):
			matrix[adjRow][adjCol] += 1

def flash(matrix, flashed):
	flashers = getAllPotentialFlashers(matrix, flashed)
	if len(flashers) > 0:
		incrementAdj(matrix, flashers)
		flashed.extend(flashers)
		flash(matrix, flashed)
	else:
		global count
		count += len(flashed)
		for (row, col) in flashed:
			matrix[row][col] = 0

for i in range(0, 100):
	increment(matrix)
	flash(matrix, [])

print("Part 1: "+str(count))

#Part 2
matrix = []
file.seek(0)
for row in file:
	line = [int(char) for char in row.strip()]
	matrix.append(line)
file.close()

def allZero(matrix):
	for row in matrix:
		for num in row:
			if num != 0: return False
	return True

round = 0
while not allZero(matrix):
	increment(matrix)
	flash(matrix, [])
	round += 1

print("Part 2: "+str(round))
