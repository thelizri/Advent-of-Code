import math

input = """..F7.
.FJ|.
SJ.L7
|F--J
LJ...""".splitlines()

input = open("day10.txt").read().splitlines()


def find_starting_position(grid: list[str]) -> tuple | None:
    for y, row in enumerate(grid):
        for x, cell in enumerate(row):
            if cell == "S":
                return (y, x)
    return None


def next_direction(char, prev_dir):
    y, x = prev_dir
    if char == "F" or char == "J":
        # 0, -1 to 1, 0
        # -1, 0 to 0, 1
        return -x, -y
    if char == "L" or char == "7":
        # 1, 0 to 0, 1
        # 0, -1 to -1, 0
        return x, y
    return prev_dir


def update_position(position, direction):
    return (position[0] + direction[0], position[1] + direction[1])


def get_char(position):
    y, x = position
    return input[y][x]


def part1(position, direction):
    count = 0
    while True:
        position = update_position(position, direction)
        count += 1
        char = get_char(position)
        if char == "S":
            return count
        if char == ".":
            return -1
        direction = next_direction(char, direction)


position = find_starting_position(input)
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
for dir in directions:
    count = part1(position, dir)
    if count != -1:
        print("Part 1:", math.ceil(count / 2))
        break
