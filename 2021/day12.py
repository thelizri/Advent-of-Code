#Your goal is to find the number of distinct paths that start at start, end at end, 
#and don't visit small caves more than once.

file = open("day12.txt", "r")
file.seek(0)

def addNode(graph, key, node):
    li = graph.get(key)
    if node not in li:
        li.append(node)

graph = dict()
for row in file:
    [a, b] = row.strip().split("-")
    if a in graph:
        addNode(graph, a, b)
    else:
        graph.update({a: [b]})
    if b in graph:
        addNode(graph, b, a)
    else:
        graph.update({b: [a]})

nodes = list(graph.keys())
nodes.remove("start")

def dfs_search(node, graph, unvisited):
    if node == "end": return 1
    neigh = graph.get(node).copy()
    if "start" in neigh: neigh.remove("start")
    total = 0
    for n in neigh:
        if n in unvisited:
            copy = unvisited.copy()
            if n.islower(): copy.remove(n)
            total += dfs_search(n, graph, copy)
    return total

part1 = dfs_search("start", graph, nodes)
print("Part 1: "+str(part1))

#Part 2 Gives wrong result
def dfs_search2(node, graph, unvisited, visited):
    if node == "end": return 1
    if node != "start" and node.islower(): visited = True

    neigh = graph.get(node).copy()
    if "start" in neigh: neigh.remove("start")

    total = 0
    for n in neigh:
        if n in unvisited:
            copy_unvisited = unvisited.copy()
            if n.islower() and visited:
                copy_unvisited.remove(n)
            total += dfs_search2(n, graph, copy_unvisited, visited)
    return total

nodes = list(graph.keys())
nodes.remove("start")

part2 = dfs_search2("start", graph, nodes, False)
print("Part 2: "+str(part2))
