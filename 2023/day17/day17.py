from heapq import heappush, heappop

input = """2413432311323
3215453535623
3255245654254
3446585845452
4546657867536
1438598798454
4457876987766
3637877979653
4654967986887
4564679986453
1224686865563
2546548887735
4322674655533""".splitlines()

input = open("day17.txt").read().splitlines()

grid = [[int(number) for number in row] for row in input]

# Heat, steps, y, x, dy, dx
pq = [(0, 0, 0, 0, 0, 0)]

seen = set()

while pq:
    heat, steps, y, x, dy, dx = heappop(pq)

    if y == len(grid) - 1 and x == len(grid[0]) - 1:
        print("Part 1:", heat)
        break

    if y < 0 or y >= len(grid) or x < 0 or x >= len(grid[0]):
        continue

    if steps > 3:
        continue

    if (y, x, dy, dx, steps) in seen:
        continue

    seen.add((y, x, dy, dx, steps))

    ny, nx = y + dy, x + dx
    if ny >= 0 and ny < len(grid) and nx >= 0 and nx < len(grid[0]):
        heappush(pq, (heat + grid[ny][nx], steps + 1, ny, nx, dy, dx))

    for ndy, ndx in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        if ndy == -dy and ndx == -dx:
            continue
        if ndy == dy and ndx == dx:
            continue

        ny, nx = y + ndy, x + ndx
        if ny >= 0 and ny < len(grid) and nx >= 0 and nx < len(grid[0]):
            heappush(pq, (heat + grid[ny][nx], 1, ny, nx, ndy, ndx))
