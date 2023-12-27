from collections import deque

input = """...........
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
    result = deque()
    while queue:
        y, x = queue.popleft()
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
            result.append((y, x))
            visited.add((y, x))
    return result


def part1(steps=64):
    start, queue = find_start(input), deque()
    queue.append(start)
    visited_odd = set()
    visited_even = set()
    for i in range(1, steps + 1):
        if i % 2 == 0:
            queue = flood_fill(input, queue, visited_even)
        else:
            queue = flood_fill(input, queue, visited_odd)

    result = len(visited_even)
    print(result)


part1()
