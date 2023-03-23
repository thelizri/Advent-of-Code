import time
import heapq
start_time = time.time()

#Goal: Find path with lowest total risk
#Can't move diagonally

#Read input
file = open("day15.txt", "r")

matrix = []
for row in file:
	line = [int(c) for c in row.strip()]
	matrix.append(line)

infinity = float("inf")
height = len(matrix)
width = len(matrix[0])

#Part 1
#Please don't look at this code. It is terrible
def validCoord(coord):
	(x, y) = coord
	if x >= 0 and x < width:
		if y >= 0 and y < height:
			return True
	return False

def getAdjacent(x, y):
	candidates = [(x+1,y), (x-1,y), (x,y+1), (x,y-1)]
	return list(filter(validCoord, candidates))

def djikstra(width, height):
	queue = []
	visited = dict()
	graph = dict()
	for y in range(height):
		for x in range(width):
			graph.update({(x,y): infinity})
			if x != 0 or y != 0:
				queue.append((infinity,x,y))
			else:
				queue.append((0,0,0))

	graph[(0,0)]=0
	heapq.heapify(queue)

	while queue:
		(dist,x,y) = heapq.heappop(queue)
		if visited.get((x,y), False): continue
		visited[(x,y)]=True
		neighbors = getAdjacent(x, y)
		for cx,cy in neighbors:#
			tempDistance = dist + matrix[cy][cx]
			distance = graph[(cx,cy)]
			if tempDistance < distance:
				graph[(cx,cy)]=tempDistance
				if (distance,cx,cy) in queue:
					heapq.heappush(queue,(tempDistance,cx,cy))

	return graph[(width-1, height-1)]


shortestPath = djikstra(width, height)
print(f"Part 1: {shortestPath}")
print(f"Time: {time.time()-start_time}")

#Part 2
#Not the most efficent approach
#Part 2 takes about 25 minutes to execute
def addTo(num, add):
	number = num+add
	if number > 9:
		number %= 9
	return number

def incrementLi(li, add):
	return list(map(lambda n: addTo(n, add), li.copy()))

#Increase matrix
for y in range(height):
	row = matrix[y]
	copy = row.copy()
	for i in range(1,5):
		copy.extend(incrementLi(row, i))
	matrix[y]=copy

for i in range(1,5):
	for y in range(height):
		row = incrementLi(matrix[y], i)
		matrix.append(row)

height = len(matrix)
width = len(matrix[0])

shortestPath = djikstra(width, height)
print(f"Part 2: {shortestPath}")
print(f"Time: {time.time()-start_time}")