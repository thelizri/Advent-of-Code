# Card x: Winning Numbers | Numbers on cards

text = """Card 1: 41 48 83 86 17 | 83 86  6 31 17  9 48 53
Card 2: 13 32 20 16 61 | 61 30 68 82 17 32 24 19
Card 3:  1 21 53 59 44 | 69 82 63 72 16 21 14  1
Card 4: 41 92 73 84 69 | 59 84 76 51 58  5 54 83
Card 5: 87 83 26 28 32 | 88 30 70 12 93 22 82 36
Card 6: 31 18 13 56 72 | 74 77 10 23 35 67 36 11
""".splitlines()

text = open("day4.txt").read().splitlines()

part1 = 0
for row_id, row in enumerate(text, 1):
    _, row = row.split(":")
    winning_numbers, card_numbers = row.split("|")
    winning_numbers, card_numbers = set(winning_numbers.split()), set(
        card_numbers.split()
    )

    amount_of_winning_numbers = len(winning_numbers.intersection(card_numbers))
    if amount_of_winning_numbers != 0:
        part1 += 2 ** (amount_of_winning_numbers - 1)

print("Part 1:", part1)

my_dict = {}
for i in range(len(text)):
    my_dict[i + 1] = 1

part2 = 0
for row_id, row in enumerate(text, 1):
    _, row = row.split(":")
    winning_numbers, card_numbers = row.split("|")
    winning_numbers, card_numbers = set(winning_numbers.split()), set(
        card_numbers.split()
    )

    amount_of_winning_numbers = len(winning_numbers.intersection(card_numbers))
    for i in range(1, amount_of_winning_numbers + 1):
        my_dict[row_id + i] = my_dict[row_id + i] + my_dict[row_id]

part2 = sum(list(my_dict.values()))
print("Part 2:", part2)
