import networkx as nx

example_input = """jqt: rhn xhk nvd
rsh: frs pzl lsr
xhk: hfx
cmg: qnr nvd lhk bvb
rhn: xhk bvb hfx
bvb: xhk hfx
pzl: lsr hfx nvd
qnr: nvd
ntq: jqt hfx bvb xhk
nvd: lhk
lsr: lhk
rzs: qnr cmg lsr rsh
frs: qnr lhk lsr""".splitlines()

input = open("day25.txt").read().splitlines()

graph = nx.Graph()
for line in input:
    a, b = line.split(": ")
    for c in b.split():
        graph.add_edge(a, c)

# Don't really know how this works, the library solves it for me
# I'll probably come back to this later
graph.remove_edges_from(nx.minimum_edge_cut(graph))
left, right = nx.connected_components(graph)
print("Part 1:", len(left) * len(right))
