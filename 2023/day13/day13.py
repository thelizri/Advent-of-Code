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


def find_horizontal_reflection_line(grid, previous):
    rows = grid.splitlines()
    total_rows = len(rows)
    for row_index, (upper_row, lower_row) in enumerate(zip(rows[:-1], rows[1:])):
        if upper_row == lower_row:
            # Check for a valid reflection line
            max_check_range = min(row_index + 1, total_rows - row_index - 1)
            is_reflection_line = True
            for offset in range(1, max_check_range):
                above_row_index, below_row_index = (
                    row_index - offset,
                    row_index + 1 + offset,
                )
                if rows[above_row_index] != rows[below_row_index]:
                    is_reflection_line = False
                    break
            if is_reflection_line:
                result = (row_index + 1) * 100
                if previous and previous != result:
                    return result
                elif not previous:
                    return result


def find_vertical_reflection_line(grid, previous):
    rows = grid.splitlines()
    row_length = len(rows[0])
    for column_index in range(row_length - 1):
        left_column = [row[column_index] for row in rows]
        right_column = [row[column_index + 1] for row in rows]
        if left_column == right_column:
            # Check for a valid reflection line
            max_check_range = min(column_index + 1, row_length - column_index - 1)
            is_reflection_line = True
            for offset in range(1, max_check_range):
                left_column_index, right_column_index = (
                    column_index - offset,
                    column_index + 1 + offset,
                )
                left_column = [row[left_column_index] for row in rows]
                right_column = [row[right_column_index] for row in rows]
                if left_column != right_column:
                    is_reflection_line = False
                    break
            if is_reflection_line:
                result = column_index + 1
                if previous and previous != result:
                    return result
                elif not previous:
                    return result


def find_reflection_line(grid, previous=None):
    reflection_line = find_horizontal_reflection_line(grid, previous)
    if reflection_line:
        return reflection_line
    else:
        reflection_line = find_vertical_reflection_line(grid, previous)
        if reflection_line:
            return reflection_line


previous_reflections = {}
reflection_sum = 0
for g, grid in enumerate(inputs):
    reflection_line = find_reflection_line(grid)
    if reflection_line:
        previous_reflections[g] = reflection_line
        reflection_sum += reflection_line

print("Part 1:", reflection_sum)

newline = "\n"
reflection_sum = 0
for g, grid in enumerate(inputs):
    found_reflection = False
    for c, ch in enumerate(grid):
        if ch not in "#.S":
            continue
        if ch == "S":
            print("S = ", c)
        if ch == "#":
            li = list(grid)
            li[c] = "."
            modified_grid = "".join(li)
        else:
            li = list(grid)
            li[c] = "#"
            modified_grid = "".join(li)
        reflection_line = find_reflection_line(modified_grid, previous_reflections[g])
        if reflection_line and reflection_line != previous_reflections[g]:
            reflection_sum += reflection_line
            found_reflection = True
            break

print("Part 2:", reflection_sum)
