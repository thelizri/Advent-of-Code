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

def getMin(queue):
	(minX, minY, minDist) = queue[0]
	for x,y,dist in queue:
		if dist < minDist:
			minX = x
			minY = y
			minDist = dist
	queue.remove((minX, minY, minDist))
	return (minX, minY, minDist)

queue = []
visited = []
graph = dict()
for y in range(height):
	for x in range(width):
		graph.update({(x,y): infinity})
		if x != 0 or y != 0:
			queue.append((x,y,infinity))
		else:
			queue.append((0,0,0))

graph[(0,0)]=0

while queue:
	(x,y,dist) = getMin(queue)
	visited.append((x,y))
	neighbors = getAdjacent(x, y)
	for cx,cy in neighbors:
		tempDistance = dist + matrix[cy][cx]
		distance = graph[(cx,cy)]
		if tempDistance < distance:
			graph[(cx,cy)]=tempDistance
			i = queue.index((cx,cy,distance))
			queue[i]=(cx,cy,tempDistance)

shortestPath = graph[(width-1, height-1)]
print(f"Part 1: {shortestPath}")


# function dijkstra(G, S)
#     for each vertex V in G
#         distance[V] <- infinite
#         previous[V] <- NULL
#         If V != S, add V to Priority Queue Q
#     distance[S] <- 0
	
#     while Q IS NOT EMPTY
#         U <- Extract MIN from Q
#         for each unvisited neighbour V of U
#             tempDistance <- distance[U] + edge_weight(U, V)
#             if tempDistance < distance[V]
#                 distance[V] <- tempDistance
#                 previous[V] <- U
#     return distance[], previous[]