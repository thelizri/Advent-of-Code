# Get input
# Parse input
# Work down until zeroes
# Predict next number
# Do the same for all rows
# Add up all predicted numbers
import re

text = """0 3 6 9 12 15
1 3 6 10 15 21
10 13 16 21 30 45""".splitlines()

text = open("day9.txt").read().splitlines()

pattern = re.compile(r"-?\d+")


def sequence_of_differences(sequence):
    result = []
    for i, j in zip(sequence[:-1], sequence[1:]):
        result.append(j - i)
    return result


def is_all_zero(sequence):
    for number in sequence:
        if number != 0:
            return False
    return True


def get_next(sequence):
    differences = sequence_of_differences(sequence)
    if is_all_zero(differences):
        return 0
    else:
        return differences[-1] + get_next(differences)


def get_prev(sequence):
    differences = sequence_of_differences(sequence)
    if is_all_zero(differences):
        return 0
    else:
        return differences[0] - get_prev(differences)


part1 = 0
part2 = 0
for row in text:
    # Convert to numbers
    row_of_numbers = [int(number) for number in re.findall(pattern, row)]
    next = get_next(row_of_numbers)
    next_number = row_of_numbers[-1] + next
    part1 += next_number
    prev = get_prev(row_of_numbers)
    prev_number = row_of_numbers[0] - prev
    part2 += prev_number

print("Part 1:", part1)
print("Part 2:", part2)
