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
vertices = []


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


for row in input:
    instruction, number, color = row.split(" ")
    number = int(number)

    pos = move(pos, instruction, number)
    vertices.append(pos)


def shoelace_area(vertices):
    """
    Calculate the area of a polygon using the Shoelace formula.

    :param vertices: A list of tuples, where each tuple represents the x and y coordinates of a vertex.
                     The vertices should be ordered clockwise or counterclockwise.
    :return: The area of the polygon.
    """
    n = len(vertices)
    area = 0

    # Sum over each edge of the polygon
    for i in range(n):
        x1, y1 = vertices[i]
        x2, y2 = vertices[(i + 1) % n]  # % n to loop back to the first vertex
        area += x1 * y2 - x2 * y1

    return abs(area) / 2


interior_area = shoelace_area(vertices)
total_area = interior_area + len(terrain) / 2 + 1
print("Part 1:", int(total_area))

# R, D, L, U
directions = {"0": (1, 0), "1": (0, 1), "2": (-1, 0), "3": (0, -1)}

# Part 2
border = 0
vertices = []
pos = (0, 0)
for row in input:
    _, _, hexacode = row.split(" ")
    dx, dy = directions[hexacode[-2]]
    length = int(hexacode[2:-2], 16)
    border += length

    pos = (pos[0] + dx * length, pos[1] + dy * length)
    vertices.append(pos)

interior_area = shoelace_area(vertices)
total_area = interior_area + border / 2 + 1
print("Part 2:", int(total_area))
