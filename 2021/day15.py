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

shortestPath = graph[(width-1, height-1)]
print(f"Part 1: {shortestPath}")

print(f"Time: {time.time()-start_time}")

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