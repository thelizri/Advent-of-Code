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

# Iterate through each edge line to parse and map the nodes
for edge in edges:
    # Split the node and its edges
    node, node_edges = edge.split(" = ")
    # Remove parentheses and spaces, then split by comma to get individual edges
    node_edges = node_edges.strip("()").replace(" ", "").split(",")
    # Map the node to its edges
    node_edges_map[node] = node_edges


node = "AAA"
part1 = None
steps = 0
while part1 is None:
    for instr in instructions:
        steps += 1
        left, right = node_edges_map[node]
        if instr == "L":
            node = left
        else:
            node = right
        if node == "ZZZ":
            part1 = steps
            break

print("Part 1:", steps)
