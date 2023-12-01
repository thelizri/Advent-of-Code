# Redefining the improved function
def get_first_and_last_number(row):
    # Mapping words to their numeric values
    word_to_number = {
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    first, last = None, None
    first_index, last_index = -1, -1

    # Check for numeric characters and update first and last accordingly
    for left_index, char in enumerate(row):
        if char.isnumeric():
            if first is None:
                first = char
                first_index = left_index
            last = char
            last_index = left_index

    # Check for numeric words and update first and last if necessary
    for word, num in word_to_number.items():
        left_index = row.find(word)
        right_index = row.rfind(word)
        if left_index != -1:
            if first is None or left_index < first_index:
                first = num
                first_index = left_index
            if last is None or right_index > last_index:
                last = num
                last_index = right_index

    return first, last


# Part 1
file = open("day1.txt")
total_sum = 0
for row in file:
    first, last = None, None
    first_index, last_index = -1, -1

    # Check for numeric characters and update first and last accordingly
    for index, char in enumerate(row):
        if char.isnumeric():
            if first is None:
                first = char
                first_index = index
            last = char
            last_index = index

    if first and last:
        number = first + last
        total_sum += int(number)
file.close()  # Close the file after reading
print(total_sum)

# Part 2
total_sum = 0
file = open("day1.txt")  # Reopen the file for Part 2
for row in file:
    first, last = get_first_and_last_number(row)
    # Default to '0' if no numeric value found
    first = first if first is not None else "0"
    last = last if last is not None else "0"
    total_sum += int(first + last)
file.close()  # Close the file after reading

print(total_sum)
