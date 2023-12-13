inputs = """#.##..##.
..#.##.#.
##......#
##......#
..#.##.#.
..##..##.
#.#.##.#.

#...##..#
#....#..#
..##..###
#####.##.
#####.##.
..##..###
#....#..#""".split(
    "\n\n"
)

inputs = open("day13.txt").read().split("\n\n")

# Determine line of reflection horizontally
# Determine line of reflection vertically
# Vertically -> Add columns to the left
# Horizontally -> Add up rows above * 100


def horizontal_reflection(grid):
    rows = grid.splitlines()
    length = len(rows)
    for r, (a, b) in enumerate(zip(rows[:-1], rows[1:])):
        if a == b:
            # Double check
            n = min(r + 1, length - r - 1)
            cond = True
            for m in range(1, n):
                a_pos, b_pos = r - m, r + 1 + m
                if rows[a_pos] != rows[b_pos]:
                    cond = False
                    break
            if cond:
                return (r + 1) * 100


def vertical_reflection(grid):
    rows = grid.splitlines()
    length = len(rows[0])
    for c in range(length - 1):
        column_a = [row[c] for row in rows]
        column_b = [row[c + 1] for row in rows]
        if column_a == column_b:
            # Double check
            n = min(c + 1, length - c - 1)
            cond = True
            for m in range(1, n):
                a_pos, b_pos = c - m, c + 1 + m
                column_a = [row[a_pos] for row in rows]
                column_b = [row[b_pos] for row in rows]
                if column_a != column_b:
                    cond = False
                    break
            if cond:
                return c + 1


total_sum = 0
for input in inputs:
    number = horizontal_reflection(input)
    if number:
        total_sum += number
    else:
        number = vertical_reflection(input)
        if number:
            total_sum += number
print(total_sum)
