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

# (S), garden plots (.), and rocks (#)
queue = deque()


def find_start(garden):
    for y, row in enumerate(garden):
        for x, cell in enumerate(row):
            if cell == "S":
                return y, x


def flood_fill(garden, queue):
    result = deque()
    while queue:
        y, x = queue.popleft()
        if y < 0 or y >= len(garden) or x < 0 or x >= len(garden[y]):
            continue
        if garden[y][x] == "#":
            continue
        for y, x in [(y + 1, x), (y - 1, x), (y, x + 1), (y, x - 1)]:
            if y < 0 or y >= len(garden) or x < 0 or x >= len(garden[y]):
                continue
            if garden[y][x] == "#":
                continue
            if (y, x) in result:
                continue
            result.append((y, x))
    return result


def part1():
    start, queue = find_start(input), deque()
    queue.append(start)
    for i in range(64):
        queue = flood_fill(input, queue)
    result = len(set(queue))
    print(result)


part1()
