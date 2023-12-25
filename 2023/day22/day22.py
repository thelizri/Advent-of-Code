from collections import deque

input = """1,0,1~1,2,1
0,0,2~2,0,2
0,2,3~2,2,3
0,0,4~0,2,4
2,0,5~2,2,5
0,1,6~2,1,6
1,1,8~1,1,9""".splitlines()


def parse_input(input):
    blocks = []
    for row in input:
        left, right = row.split("~")
        left = [int(x) for x in left.split(",")]
        right = [int(x) for x in right.split(",")]
        blocks.append((left, right))

    return blocks


def intersection_rectangles(rect1, rect2):
    start1, end1 = rect1
    start2, end2 = rect2
    x1, y1, _ = start1
    xend1, yend1, _ = end1
    x2, y2, _ = start2
    xend2, yend2, _ = end2

    x = max(x1, x2)
    xend = min(xend1, xend2)
    if xend <= x:
        return False

    y = max(y1, y2)
    yend = min(yend1, yend2)
    if yend <= y:
        return False

    return True


def sort_blocks(blocks):
    blocks.sort(key=lambda x: x[0][2])
    return blocks


blocks = parse_input(input)
blocks = sort_blocks(blocks)
print(blocks)
# Make rectangles fall
# Find which can be vaproized
