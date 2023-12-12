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

input_data = open("day11.txt").read().splitlines()

# Convert the input data into a list of lists for easy manipulation
grid = [list(row) for row in input_data]

# Function to insert an empty row
def insert_empty_row(grid, row_index):
    empty_row = ['.' for _ in range(len(grid[0]))]
    grid.insert(row_index + 1, empty_row)

# Function to insert an empty column
def insert_empty_column(grid, col_index):
    for row in grid:
        row.insert(col_index + 1, '.')

# Identify and insert empty rows
empty_rows = [r for r, row in enumerate(grid) if all(ch == '.' for ch in row)]
for i in reversed(empty_rows):  # Use reversed to avoid indexing issues
    insert_empty_row(grid, i)

# Identify and insert empty columns
empty_columns = [c for c in range(len(grid[0])) if all(row[c] == '.' for row in grid)]
for i in reversed(empty_columns):  # Use reversed to avoid indexing issues
    insert_empty_column(grid, i)

count = 1
galaxy_coordinates = {}
for r, row in enumerate(grid):
    for c, ch in enumerate(row):
        if ch == "#":
            galaxy_coordinates[count] = (r, c)
            count += 1

total_path = 0
for a in range(1, count-1):
    for b in range(a+1, count):
        a_y, a_x = galaxy_coordinates[a]
        b_y, b_x = galaxy_coordinates[b]
        total_path += abs(a_y - b_y) + abs(a_x - b_x)

print("Part 1:", total_path)