import math

input = """FF7FSF7F7F7F7F7F---7
L|LJ||||||||||||F--J
FL-7LJLJ||||||LJL-77
F--JF--7||LJLJ7F7FJ-
L---JF-JLJ.||-FJLJJ7
|F|F-JF---7F7-L7L|7|
|FFJF7L7F-JF7|JL---7
7-L-JL7||F7|L7F-7F7|
L.L7LFJ|||||FJL7||LJ
L7JLJL-JLJLJL--JLJ.L""".splitlines()

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


def get_trail_length(position, direction):
    count, trail = 0, set()
    while True:
        count += 1
        position = update_position(position, direction)
        trail.add(position)
        char = get_char(position)
        if char == "S":
            return count, trail
        if char == ".":
            return -1, None
        direction = next_direction(char, direction)


position = find_starting_position(input)
directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
trail = None
for dir in directions:
    count, trail = get_trail_length(position, dir)
    if count != -1:
        print("Part 1:", math.ceil(count / 2))
        break

# Replace all pipes outside the loop with #
grid = []
for r, row in enumerate(input):
    new_row = []
    for c, ch in enumerate(row):
        if (r, c) in trail:
            new_row.append(ch)  # Keep the character if it's in the trail or a period
        else:
            new_row.append("#")  # Replace '|' with '#' otherwise
    grid.append("".join(new_row))


count = 0


def check_left(r, c):
    count = 0
    up = False
    down = False
    for x in range(c):
        char = grid[r][x]
        if char in "|":
            count += 1
        elif char in "F7":
            down = not down
        elif char in "LJ":
            up = not up
        if up and down:
            count += 1
            up, down = False, False

    return count % 2 == 1


def check_right(r, c, length):
    count = 0
    up = False
    down = False
    for x in range(c, length):
        char = grid[r][x]
        if char in "|":
            count += 1
        elif char in "F7":
            down = not down
        elif char in "LJ":
            up = not up
        if up and down:
            count += 1
            up, down = False, False

    return count % 2 == 1


for r, row in enumerate(grid):
    if r == 0 or r == len(grid) - 1:
        continue
    for c, char in enumerate(row):
        if c == 0 or c == len(row) - 1:
            continue
        if char != "#":
            continue
        if check_left(r, c) and check_right(r, c, len(row)):
            count += 1

print("Part 2:", count)
