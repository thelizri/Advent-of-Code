from collections import deque
import re

input = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9""".splitlines()


def parse_input(input):
    pattern = r"\d+"
    blocks = []
    for row in input:
        matches = re.findall(pattern, row)
        block = [int(x) for x in matches]
        block[3] += 1
        block[4] += 1
        blocks.append(block)

    return blocks


def intersection(rect1, rect2):
    x1, y1, _, xe1, ye1, _ = rect1
    x2, y2, _, xe2, ye2, _ = rect2
    x = max(x1, x2)
    xend = min(xe1, xe2)
    if x >= xend:
        return False

    y = max(y1, y2)
    yend = min(ye1, ye2)
    if y >= yend:
        return False

    return True


def sort_blocks(blocks):
    blocks.sort(key=lambda x: x[2])
    return blocks


def falling(blocks):
    for i, block in enumerate(blocks):
        minz, z = 1, block[2]
        for block2 in blocks[:i]:
            if intersection(block, block2):
                minz = max(minz, block2[5] + 1)

        if z > minz:
            diff = z - minz
            block[2] -= diff
            block[5] -= diff


def part1(blocks):
    supported = {i: [] for i in range(len(blocks))}
    support = {i: [] for i in range(len(blocks))}
    for i, block in enumerate(blocks):
        z1 = block[5]
        for j, block2 in enumerate(blocks[i + 1 :], i + 1):
            z2 = block2[2]
            if z2 <= z1:
                continue
            if z2 > z1 + 1:
                break
            if intersection(block, block2):
                supported[j].append(i)
                support[i].append(j)

    count = 0
    for value in support.values():
        if len(value) == 0:
            count += 1
        else:
            has_support = True
            for j in value:
                if len(supported[j]) <= 1:
                    has_support = False
                    break
            if has_support:
                count += 1

    print("Part 1:", count)


blocks = parse_input(input)
sort_blocks(blocks)
falling(blocks)
part1(blocks)
