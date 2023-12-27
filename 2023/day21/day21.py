from collections import deque

example_input = """...........
.....###.#.
.###.##..#.
..#.#...#..
....#.#....
.##..S####.
.##..#...#.
.......##..
.##.#.####.
.##..##.##.
...........""".splitlines()

input = open("day21.txt").read().splitlines()
height, width = len(input), len(input[0])

# (S), garden plots (.), and rocks (#)
queue = deque()


def find_start(garden):
    for y, row in enumerate(garden):
        for x, cell in enumerate(row):
            if cell == "S":
                return y, x


def flood_fill(garden, queue, visited):
    while queue:
        y, x, steps = queue.popleft()
        if y < 0 or y >= height or x < 0 or x >= width:
            continue
        if garden[y][x] == "#":
            continue

        for y, x in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
            if y < 0 or y >= height or x < 0 or x >= width:
                continue
            if garden[y][x] == "#":
                continue
            if (y, x) in visited:
                continue
            if steps > 0:
                queue.append((y, x, steps - 1))
            if (steps - 1) % 2 == 0:
                visited.add((y, x))

    return visited


def part1(input=input, steps=64):
    (y, x), queue = find_start(input), deque()

    queue.append((y, x, steps))
    visited = flood_fill(input, queue, set())

    result = len(visited)
    print(result)


part1()

# Part 2
# Reachable tiles = a*steps^2 + b*steps + c
# 65 steps, 131*n steps
# Note that 26501365 // 131 == 202300. I.e. this is the number of tile lengths that we can move away from the centre in a straight line, given this number of steps.
# Also, 26501365 % 131 == 65. So, we can move exactly 202300 and one half complete tile distances from the centre.
