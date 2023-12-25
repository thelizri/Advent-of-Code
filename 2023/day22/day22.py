from collections import deque
import re

input = """1,0,1~1,2,1
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
sort_blocks(blocks)
part1(blocks)
