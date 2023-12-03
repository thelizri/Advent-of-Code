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

print(part1)
