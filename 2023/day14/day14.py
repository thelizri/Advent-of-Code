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


def calc_load(grid):
    load = 0
    for r, row in enumerate(reversed(grid), 1):
        load += row.count("O") * r
    return load


grid = parse_input(input)
grid = tilt_nort(grid)
load = calc_load(grid)
print("Part 1:", load)
