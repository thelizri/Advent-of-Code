from collections import deque
import re

example_input = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9""".splitlines()

input = open("day22.txt", "r").read().splitlines()


def parse_input(input):
    pattern = r"\d+"
    blocks = []
    for row in input:
        matches = re.findall(pattern, row)
        block = [int(x) for x in matches]
        blocks.append(block)

    return blocks


def intersection(rect1, rect2):
    if max(rect1[0], rect2[0]) > min(rect1[3], rect2[3]):
        return False

    if max(rect1[1], rect2[1]) > min(rect1[4], rect2[4]):
        return False

    return True


def sort_blocks(blocks):
    blocks.sort(key=lambda x: x[2])
    return blocks


def falling(blocks):
    for index, block in enumerate(blocks):
        maxz = 1
        for block2 in blocks[:index]:
            if intersection(block, block2):
                maxz = max(maxz, block2[5] + 1)

        block[5] += maxz - block[2]
        block[2] = maxz


def get_structure(blocks):
    j_issupportedby_i = {i: [] for i in range(len(blocks))}
    i_supports_j = {i: [] for i in range(len(blocks))}
    for i, block in enumerate(blocks):
        z1 = block[5]
        for j, block2 in enumerate(blocks[i + 1 :], i + 1):
            z2 = block2[2]
            if z2 <= z1:
                continue
            if z2 > z1 + 1:
                break
            if intersection(block, block2):
                j_issupportedby_i[j].append(i)
                i_supports_j[i].append(j)
    return j_issupportedby_i, i_supports_j


def part1(input):
    blocks = parse_input(input)
    sort_blocks(blocks)
    falling(blocks)
    sort_blocks(blocks)
    j_issupportedby_i, i_supports_j = get_structure(blocks)

    count = 0
    for supported_blocks in i_supports_j.values():
        if len(supported_blocks) == 0 or all(
            [len(j_issupportedby_i[j]) >= 2 for j in supported_blocks]
        ):
            count += 1

    print("Part 1:", count)


def part2(input):
    blocks = parse_input(input)
    sort_blocks(blocks)
    falling(blocks)
    sort_blocks(blocks)
    j_issupportedby_i, i_supports_j = get_structure(blocks)

    def count_falling(i):
        falling = set()
        falling.add(i)
        queue = deque(i_supports_j[i])
        while queue:
            block = queue.popleft()
            support = j_issupportedby_i[block]
            if all([x in falling for x in support]):
                falling.add(block)
                queue.extend(i_supports_j[block])
        return len(falling) - 1

    count = 0
    for key in i_supports_j.keys():
        count += count_falling(key)

    print("Part 2:", count)


part1(input)
part2(input)
