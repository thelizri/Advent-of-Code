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

print(graph)