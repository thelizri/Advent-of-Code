import sys
from collections import deque

input = """#.#####################
#.......#########...###
#######.#########.#.###
###.....#.>.>.###.#.###
###v#####.#v#.###.#.###
###.>...#.#.#.....#...#
###v###.#.#.#########.#
###...#.#.#.......#...#
#####.#.#.#######.#.###
#.....#.#.#.......#...#
#.#####.#.#.#########v#
#.#...#...#...###...>.#
#.#.#v#######v###.###v#
#...#.>.#...>.>.#.###.#
#####v#.#.###v#.#.###.#
#.....#...#...#.#.#...#
#.#########.###.#.#.###
#...###...#...#...#.###
###.###.#.###v#####v###
#...#...#.#.>.>.#.>.###
#.###.###.#.###.#.#v###
#.....###...###...#...#
#####################.#
""".splitlines()

input = open("day23.txt").read().splitlines()

start = (0, 1)
end = (len(input) - 1, len(input[0]) - 2)
visited = set()

sys.setrecursionlimit(3000)


def part1(y, x, steps, visited):
    # Check boundaries and walls first
    if y < 0 or y >= len(input) or x < 0 or x >= len(input[0]) or input[y][x] == "#":
        return 0
    # Check if the end is reached
    if (y, x) == end:
        return steps
    # Check if already visited
    if (y, x) in visited:
        return 0

    visited.add((y, x))

    max_steps = 0
    if input[y][x] in "^v<>":
        if input[y][x] == "^":
            ny, nx = y - 1, x
        elif input[y][x] == "v":
            ny, nx = y + 1, x
        elif input[y][x] == "<":
            ny, nx = y, x - 1
        elif input[y][x] == ">":
            ny, nx = y, x + 1
        max_steps = max(max_steps, part1(ny, nx, steps + 1, visited))
    else:
        for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
            if (ny, nx) not in visited:
                max_steps = max(max_steps, part1(ny, nx, steps + 1, visited))

    visited.remove((y, x))
    return max_steps


result = part1(start[0], start[1], 0, set())
print("Part 1:", result)


# Part 2
def prune_grid():
    points = []
    for y, row in enumerate(input):
        for x, c in enumerate(row):
            if c == "#":
                continue
            outgoing = 0
            for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
                if ny < 0 or ny >= len(input) or nx < 0 or nx >= len(input[0]):
                    continue
                if input[ny][nx] == "#":
                    continue
                outgoing += 1
            if outgoing > 2:
                points.append((y, x))
    return points


def find_adjacent_points(y, x, points):
    points = points.copy()
    points.remove((y, x))
    adjacent = []
    queue = deque([(y, x, 0)])
    visited = set()
    while queue:
        y, x, steps = queue.popleft()
        visited.add((y, x))
        for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
            if ny < 0 or ny >= len(input) or nx < 0 or nx >= len(input[0]):
                continue
            if input[ny][nx] == "#":
                continue
            if (ny, nx) in points:
                adjacent.append((ny, nx, steps + 1))
            if (ny, nx) not in visited and (ny, nx) not in points:
                queue.append((ny, nx, steps + 1))
    return adjacent


points = prune_grid()
points.append(start)
points.append(end)
graph = {}
for pos in points:
    graph[pos] = find_adjacent_points(pos[0], pos[1], points)


def depth_first_search(graph, start, end, length, visited=set()):
    if start == end:
        return length

    visited.add(start)

    max_steps = 0
    for y, x, steps in graph[start]:
        if (y, x) not in visited:
            max_steps = max(
                max_steps,
                depth_first_search(graph, (y, x), end, length + steps, visited),
            )

    visited.remove(start)
    return max_steps


part2 = depth_first_search(graph, start, end, 0, set())
print("Part 2:", part2)
