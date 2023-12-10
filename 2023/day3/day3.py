import re

text = """467..114..
...*......
..35..633.
......#...
617*......
.....+.58.
..592.....
......755.
...$.*....
.664.598..
"""

text = open("day3.txt").read()

grid = text.splitlines()

part1 = 0


def extract_numbers_with_positions(text):
    pattern = r"\d+"
    matches = re.finditer(pattern, text)
    return [(match.group(), match.start()) for match in matches]


def is_symbol(char):
    if char not in ["0", "1", "2", "3", "4", "5", "6", "7", "8", "9", "."]:
        return True
    return False


def is_adjacent(row_id, x):
    adj = [-1, 1, 0]
    for row_mod in adj:
        for x_mod in adj:
            try:
                if is_symbol(grid[row_id + row_mod][x + x_mod]):
                    return True
            except:
                pass

    return False


def extract_numbers(row_id, row):
    global part1
    numbers_with_positions = extract_numbers_with_positions(row)
    for number, pos in numbers_with_positions:
        for i in range(len(number)):
            if is_adjacent(row_id, pos + i):
                part1 += int(number)
                break


for row_id, row in enumerate(grid):
    extract_numbers(row_id, row)

print("Part 1:", part1)

part2 = 0


def gear_in_range_of_number(gear_row, gear_x, number_row, number_x, number):
    length = len(number)
    if gear_row >= number_row - 1 and gear_row <= number_row + 1:
        if gear_x >= number_x - 1 and gear_x <= number_x + length:
            return True
    return False


def is_gear(row_id, x):
    numbers = []
    global part2
    for i in [-1, 0, 1]:
        numbers_with_positions = extract_numbers_with_positions(grid[row_id + i])
        for number, pos in numbers_with_positions:
            # Check if number is within distance of gear
            if gear_in_range_of_number(row_id, x, row_id + i, pos, number):
                numbers.append(number)

    if len(numbers) == 2:
        part2 += int(numbers[0]) * int(numbers[1])


for row_id, row in enumerate(grid):
    for x, char in enumerate(row):
        if char == "*":
            is_gear(row_id, x)

print("Part 2:", part2)
