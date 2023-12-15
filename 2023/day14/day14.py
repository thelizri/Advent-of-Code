input = """O....#....
O.OO#....#
.....##...
OO.#O....O
.O.....O#.
O.#..O.#.#
..O..#O..O
.......O..
#....###..
#OO..#....""".splitlines()

input = open("day14.txt").read().splitlines()


def parse_input(input_string):
    return [list(line) for line in input_string]


def tilt_nort(grid):
    for col_id in range(len(grid[0])):
        for row_id in range(1, len(grid)):
            if grid[row_id][col_id] == "O":
                # Move rock as far upwards as possible
                final_destination = row_id
                while (
                    final_destination > 0 and grid[final_destination - 1][col_id] == "."
                ):
                    final_destination -= 1
                # Switch places between rock and empty space
                if final_destination != row_id:
                    grid[final_destination][col_id] = "O"
                    grid[row_id][col_id] = "."
    return grid


def tilt_south(grid):
    for col_id in range(len(grid[0])):
        for row_id in reversed(range(len(grid) - 1)):
            if grid[row_id][col_id] == "O":
                # Move rock as far downwards as possible
                final_destination = row_id
                while (
                    final_destination < len(grid) - 1
                    and grid[final_destination + 1][col_id] == "."
                ):
                    final_destination += 1
                # Switch places between rock and empty space
                if final_destination != row_id:
                    grid[final_destination][col_id] = "O"
                    grid[row_id][col_id] = "."
    return grid


def tilt_west(grid):
    for row in grid:
        for col_id in range(1, len(row)):
            if row[col_id] == "O":
                # Move rock as far left as possible
                final_destination = col_id
                while final_destination > 0 and row[final_destination - 1] == ".":
                    final_destination -= 1
                # Switch places between rock and empty space
                if final_destination != col_id:
                    row[final_destination] = "O"
                    row[col_id] = "."
    return grid


def tilt_east(grid):
    for row in grid:
        for col_id in reversed(range(len(row) - 1)):
            if row[col_id] == "O":
                # Move rock as far right as possible
                final_destination = col_id
                while (
                    final_destination < len(row) - 1
                    and row[final_destination + 1] == "."
                ):
                    final_destination += 1
                # Switch places between rock and empty space
                if final_destination != col_id:
                    row[final_destination] = "O"
                    row[col_id] = "."
    return grid


def calc_load(grid):
    load = 0
    for r, row in enumerate(reversed(grid), 1):
        load += row.count("O") * r
    return load


def make_copy(grid):
    return [row.copy() for row in grid]


def compare_grids(grid_a, grid_b):
    for a, b in zip(grid_a, grid_b):
        if a != b:
            return False
    return True


def grid_to_string(grid):
    return "\n".join("".join(row) for row in grid)


def cycle(grid):
    grid = tilt_nort(grid)
    grid = tilt_west(grid)
    grid = tilt_south(grid)
    grid = tilt_east(grid)
    return grid


grid = parse_input(input)
grid = tilt_nort(grid)
load = calc_load(grid)
print("Part 1:", load)


def part2():
    grid = parse_input(input)
    states = set(grid_to_string(grid))
    states_to_index = {grid_to_string(grid): 0}

    cycles = 0
    cycle_length = -1
    while True:
        grid = cycle(grid)
        cycles += 1

        current_state = grid_to_string(grid)
        if current_state in states:
            cycle_length = cycles - states_to_index[current_state]
            break
        else:
            states.add(current_state)
            states_to_index[current_state] = cycles

    remaining_cycles = (1_000_000_000 - cycles) % cycle_length
    for _ in range(remaining_cycles):
        grid = cycle(grid)

    load = calc_load(grid)
    print("Part 2:", load)


part2()

# Beginning state, Cycle state, Cycle length
