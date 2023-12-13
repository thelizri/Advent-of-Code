input_data = """...#......
.......#..
#.........
..........
......#...
.#........
.........#
..........
.......#..
#...#.....""".splitlines()

# input_data = open("day11.txt").read().splitlines()

# Convert the input data into a list of lists for easy manipulation
grid = [list(row) for row in input_data]

# Identify and insert empty rows
empty_rows = [r for r, row in enumerate(grid) if all(ch == "." for ch in row)]

# Identify and insert empty columns
empty_columns = [c for c in range(len(grid[0])) if all(row[c] == "." for row in grid)]

galaxies_p1 = {}


count = 1
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == "#":
            galaxies_p1[count] = (r, c)
            count += 1

copy = galaxies_p1.copy()


def expand_rows_columns(galaxies, number=1):
    # Increase rows
    for r, row in enumerate(empty_rows):
        for pos in range(1, count):
            y, x = galaxies[pos]
            if y > row + r * number:
                galaxies[pos] = (y + number, x)

    # Increase columns
    for c, col in enumerate(empty_columns):
        for pos in range(1, count):
            y, x = galaxies[pos]
            if x > col + c * number:
                galaxies[pos] = (y, x + number)


def calc_sum(galaxies):
    total_sum = 0
    for a in range(1, count - 1):
        for b in range(a + 1, count):
            a_y, a_x = galaxies[a]
            b_y, b_x = galaxies[b]
            total_sum += abs(a_y - b_y) + abs(a_x - b_x)
    return total_sum


expand_rows_columns(galaxies_p1)
print("Part 1:", calc_sum(galaxies_p1))
expand_rows_columns(copy, 10)
print("Part 2:", calc_sum(copy))
