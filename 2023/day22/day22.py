from collections import deque
import re

input = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3""".splitlines()


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


blocks = parse_input(input)
blocks = sort_blocks(blocks)
