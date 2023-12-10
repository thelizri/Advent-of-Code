import numpy as np

(
    instructions,
    edges_str,
) = """LLR

AAA = (BBB, BBB)
BBB = (AAA, ZZZ)
ZZZ = (ZZZ, ZZZ)""".split(
    "\n\n"
)

instructions, edges_str = open("day8.txt").read().split("\n\n")

# Split the input to separate the edges
edges = edges_str.splitlines()

# Initialize an empty dictionary to store the mapping of nodes to their edges
node_edges_map = {}

part2_starting_nodes = []

# Iterate through each edge line to parse and map the nodes
for edge in edges:
    # Split the node and its edges
    node, node_edges = edge.split(" = ")
    if node[2] == "A":
        part2_starting_nodes.append(node)
    # Remove parentheses and spaces, then split by comma to get individual edges
    node_edges = node_edges.strip("()").replace(" ", "").split(",")
    # Map the node to its edges
    node_edges_map[node] = node_edges


def get_distance(node="AAA", part2=False):
    steps = 0
    while True:
        for instr in instructions:
            steps += 1
            left, right = node_edges_map[node]
            if instr == "L":
                node = left
            else:
                node = right
            if part2 and node[2] == "Z":
                return steps
            if node == "ZZZ":
                return steps


print("Part 1:", get_distance())

distances = []
for node in part2_starting_nodes:
    distances.append(get_distance(node, True))

lcm = np.lcm.reduce(distances)
print("Part 2:", lcm)
