#Goal: Find path with lowest total risk
#Can't move diagonally

#Read input
file = open("day15.txt", "r")

matrix = []
for row in file:
	line = [int(c) for c in row.strip()]
	matrix.append(line)

print(matrix)

height = len(matrix)
width = len(matrix[0])

#Part 1
def validCoord(coord):
	(x, y) = coord
	if x >= 0 and x < width:
		if y >= 0 and y < height:
			return True
	return False

def getAdjacent(x, y):
	candidates = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
	return list(filter(validCoord, candidates))

def dfs_search(x, y, score, visited):
	if score > 50: return float("inf")
	score += matrix[y][x]
	visited.append((x, y))

	if x == width-1 and y == height-1:
		return score

	candidates = getAdjacent(x, y)
	neighbors = list(filter(lambda x: x not in visited, candidates))
	if neighbors:
		results = []
		for x,y in neighbors:
			results.append(dfs_search(x, y, score, visited.copy()))
		return min(results)
	else:
		return float("inf")

print(dfs_search(0, 0, -1, []))