from collections import deque

input = """R 6 (#70c710)
D 5 (#0dc571)
L 2 (#5713f0)
D 2 (#d2c081)
R 2 (#59c680)
D 2 (#411b91)
L 5 (#8ceee2)
U 2 (#caa173)
L 1 (#1b58a2)
U 2 (#caa171)
R 2 (#7807d2)
U 3 (#a77fa3)
L 2 (#015232)
U 2 (#7a21e3)""".splitlines()

input = open("day18.txt").read().splitlines()

pos = (0, 0)
terrain = set()
terrain.add(pos)


def move(pos, direction, steps):
    x, y = pos
    if direction == "R":
        for i in range(1, steps + 1):
            terrain.add((x + i, y))
        return (x + steps, y)
    elif direction == "L":
        for i in range(1, steps + 1):
            terrain.add((x - i, y))
        return (x - steps, y)
    elif direction == "U":
        for i in range(1, steps + 1):
            terrain.add((x, y - i))
        return (x, y - steps)
    elif direction == "D":
        for i in range(1, steps + 1):
            terrain.add((x, y + i))
        return (x, y + steps)


def print_map():
    max_x = max(terrain, key=lambda x: x[0])[0]
    max_y = max(terrain, key=lambda x: x[1])[1]
    print("Max:", max_x, max_y)
    for y in range(max_y + 1):
        for x in range(max_x + 1):
            if (x, y) in terrain:
                print("#", end="")
            else:
                print(".", end="")
        print()


def write_map_to_file(filename):
    min_x = min(terrain, key=lambda x: x[0])[0]
    min_y = min(terrain, key=lambda x: x[1])[1]
    max_x = max(terrain, key=lambda x: x[0])[0]
    max_y = max(terrain, key=lambda x: x[1])[1]

    with open(filename, "w") as file:
        file.write(f"Max: {max_x} {max_y}\n")
        for y in range(min_y, max_y + 1):
            file.write(str(y) + " ")
            for x in range(min_x, max_x + 1):
                if (x, y) in terrain:
                    file.write("#")
                else:
                    file.write(".")
            file.write("\n")


def flood_fill(pos):
    queue = deque()
    queue.append(pos)
    while queue:
        x, y = queue.popleft()
        if (x, y) not in terrain:
            terrain.add((x, y))
            queue.append((x + 1, y))
            queue.append((x - 1, y))
            queue.append((x, y + 1))
            queue.append((x, y - 1))
    return len(terrain)


for row in input:
    instruction, number, color = row.split(" ")
    number = int(number)

    pos = move(pos, instruction, number)

# Didn't know where to start flood fill, so I printed the map to a file and looked at it. It's a hacky solution, but it works.
# There's a math formula for calculating the interior area of a polygon, that could also be used.
length = flood_fill((1, 0))
print("Part 1:", length)
