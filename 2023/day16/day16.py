from functools import lru_cache

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


@lru_cache(maxsize=None)
def move(pos, previous_direction):
    if outofbounds(pos):
        return []

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
    result = []
    if split:
        for d in new_direction:
            new_pos = (pos[0] + d[0], pos[1] + d[1])
            result.append((new_pos, d))
    else:
        new_pos = (pos[0] + new_direction[0], pos[1] + new_direction[1])
        result.append((new_pos, new_direction))

    return result


def part1():
    energized_tiles = set()  # (y, x)
    pos, direction = (0, 0), dir["R"]
    energized_tiles.add(pos)

    pos_direction = move(pos, direction)

    cycles = 0
    while pos_direction:
        new_pos_direction = []
        new_tiles = False
        for p, d in pos_direction:
            if p not in energized_tiles and not outofbounds(p):
                energized_tiles.add(p)
                new_tiles = True
            new_pos_direction.extend(move(p, d))
        if not new_tiles:
            cycles += 1
        if cycles > 10:
            break
        pos_direction = new_pos_direction

    print("Part 1:", len(energized_tiles))


part1()
