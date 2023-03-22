#Goal: Find path with lowest total risk
#Can't move diagonally

#Read input
file = open("day15.txt", "r")

matrix = []
for row in file:
	row.strip()
	line = list(row)
	matrix.append(line)

print(matrix)

height = len(matrix)
width = len(matrix[0])

def validCoord(coord):
	(x, y) = coord
	if x >= 0 and x < width:
		if y >= 0 and y < height:
			return True
	return False

def getAdjacent(x, y):
	candidates = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
	return list(filter(validCoord, candidates))

print(getAdjacent(1, 0))