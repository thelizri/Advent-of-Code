import sys

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

# input = open("day23.txt").read().splitlines()

start = (0, 1)
end = (len(input) - 1, len(input[0]) - 2)
visited = set()

sys.setrecursionlimit(10000)


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


def part2(y, x, steps, visited):
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

    for ny, nx in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
        if (ny, nx) in visited:
            continue
        max_steps = max(max_steps, part2(ny, nx, steps + 1, visited))

    visited.remove((y, x))
    return max_steps


result = part1(start[0], start[1], 0, set())
print("Part 1:", result)
result = part2(start[0], start[1], 0, set())
print("Part 2:", result)
