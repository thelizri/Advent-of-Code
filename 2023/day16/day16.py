from collections import deque

input = r""".|...\....
|.-.\.....
.....|-...
........|.
..........
.........\
..../.\\..
.-.-/..|..
.|....-|.\
..//.|....
""".splitlines()

input = open("day16.txt").read().splitlines()

q = deque()

dir = {"U": (-1, 0), "D": (1, 0), "R": (0, 1), "L": (0, -1)}

max_x, max_y = len(input[0]), len(input)


def mirror(type, direction):
    if type == "/":
        if direction == dir["U"]:
            return dir["R"]
        if direction == dir["D"]:
            return dir["L"]
        if direction == dir["R"]:
            return dir["U"]
        if direction == dir["L"]:
            return dir["D"]
    elif type == "\\":
        if direction == dir["U"]:
            return dir["L"]
        if direction == dir["D"]:
            return dir["R"]
        if direction == dir["R"]:
            return dir["D"]
        if direction == dir["L"]:
            return dir["U"]
    else:
        raise ValueError


def splitter(type, direction):
    if type == "-":
        if direction == dir["U"] or direction == dir["D"]:
            return dir["L"], dir["R"]
        else:
            return None
    elif type == "|":
        if direction == dir["R"] or direction == dir["L"]:
            return dir["U"], dir["D"]
        else:
            return None
    else:
        raise ValueError


def outofbounds(pos):
    return pos[0] < 0 or pos[0] >= max_y or pos[1] < 0 or pos[1] >= max_x


def move(pos, previous_direction):
    tile = input[pos[0]][pos[1]]
    split = False
    if tile == ".":
        new_direction = previous_direction
    elif tile in "|-":
        new_direction = splitter(tile, previous_direction)
        if new_direction is None:
            new_direction = previous_direction
        else:
            split = True
    elif tile in "/\\":
        new_direction = mirror(tile, previous_direction)
        if new_direction is None:
            new_direction = previous_direction

    if split:
        for d in new_direction:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            q.append((new_pos, d))
    else:
        new_pos = (pos[0] + new_direction[0], pos[1] + new_direction[1])
        q.append((new_pos, new_direction))


def calc(pos=(0, 0), direction=dir["R"]):
    q.clear()
    seen_states = set()
    q.append((pos, direction))
    while q:
        pos, direction = q.popleft()
        if outofbounds(pos):
            continue
        if (pos, direction) in seen_states:
            continue
        seen_states.add((pos, direction))
        move(pos, direction)

    tiles = set()
    for pos, _ in seen_states:
        tiles.add(pos)

    return len(tiles)


print("Part 1:", calc())

# Part 2
result = []
for x in range(max_x):
    result.append(calc((0, x), dir["D"]))
    result.append(calc((max_y - 1, x), dir["U"]))
for y in range(max_y):
    result.append(calc((y, 0), dir["R"]))
    result.append(calc((y, max_x - 1), dir["L"]))
print("Part 2:", max(result))
