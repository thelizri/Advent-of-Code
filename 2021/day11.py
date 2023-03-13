file = open("day11.txt", "r")

matrix = []
for row in file:
	line = [int(char) for char in row.strip()]
	matrix.append(line)

def validCoord(coord):
	(row, col) = coord
	if row < 0 or row > 9: return False
	elif col < 0 or row > 9: return False
	return True

def getAdjacent(row, col):
	adj = [(row, col+1), (row, col-1), (row+1, col), (row-1, col),
	(row+1, col+1), (row+1, col-1), (row-1, col+1), (row-1, col-1)]
	return list(filter(validCoord, adj))

