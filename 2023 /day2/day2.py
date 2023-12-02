# Limits
# 12 Red, 13 Green, 14 Blue

import re

# Example input data used for debugging
text = """
Game 1: 3 blue, 4 red; 1 red, 2 green, 6 blue; 2 green
Game 2: 1 blue, 2 green; 3 green, 4 blue, 1 red; 1 green, 1 blue
Game 3: 8 green, 6 blue, 20 red; 5 blue, 4 red, 13 green; 5 green, 1 red
Game 4: 1 green, 3 red, 6 blue; 3 green, 6 red; 3 green, 15 blue, 14 red
Game 5: 6 red, 1 blue, 3 green; 2 blue, 1 red, 2 green
"""

text = open("day2.txt").read()

# Regex pattern to extract the amounts of blue, green, and red for each game
pattern = r"Game (\d+):((?:(?: \d+ (?:blue|green|red),?)+;?)+)"

# Find all matches
matches = re.findall(pattern, text)

# The max values of the game
max_values = {
    "blue": 14,
    "green": 13,
    "red": 12,
}

# Dictionary to store the extracted data
game_data = {}

# Process each match to extract and sum the amounts of each color for each game
for match in matches:
    game_number = int(match[0])
    game_contents = match[1]

    # Finding all color and amount pairs in the current game's contents
    color_amounts = re.findall(r"(\d+) (blue|green|red)", game_contents)

    # Summing the amounts for each color
    blue_total = max(int(amount) for amount, color in color_amounts if color == "blue")
    green_total = max(
        int(amount) for amount, color in color_amounts if color == "green"
    )
    red_total = max(int(amount) for amount, color in color_amounts if color == "red")

    # Storing the results in the dictionary
    game_data[game_number] = {
        "blue": blue_total,
        "green": green_total,
        "red": red_total,
    }

the_sum = 0
sum_of_power = 0
for game_number, color_values in game_data.items():
    part1 = True
    if color_values["blue"] > max_values["blue"]:
        part1 = False
    elif color_values["green"] > max_values["green"]:
        part1 = False
    elif color_values["red"] > max_values["red"]:
        part1 = False
    if part1:
        the_sum += game_number
    sum_of_power += color_values["blue"] * color_values["green"] * color_values["red"]


print("Part 1:", the_sum)
print("Part 2:", sum_of_power)
