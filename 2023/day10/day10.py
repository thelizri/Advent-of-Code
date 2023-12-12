import math

input = """-----
..F..
..F7.
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
        if (r, c) in trail or ch == ".":
            new_row.append(ch)  # Keep the character if it's in the trail or a period
        else:
            new_row.append("#")  # Replace '|' with '#' otherwise
    grid.append("".join(new_row))


print("\n".join(grid))
