input = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7"

input = open("day15.txt").read()


def hash(string_input):
    current_value = 0
    for ch in string_input:
        current_value += ord(ch)
        current_value *= 17
        current_value %= 256

    return current_value


amount = 0
for str in input.split(","):
    amount += hash(str)

print("Part 1:", amount)


def focusing_power(box_number, contents):
    total = 0
    for slot_number, (_, focal_length) in enumerate(contents, 1):
        total += box_number * slot_number * focal_length
    return total


boxes = {}
for i in range(256):
    boxes[i] = []

for instruction in input.split(","):
    if "-" in instruction:
        label = instruction[:-1]
        box_number = hash(label)
        contents = boxes[box_number]
        matches = [(l, f) for l, f in contents if label == l]
        for match in matches:
            contents.remove(match)
    else:
        label, number = instruction.split("=")
        box_number = hash(label)
        contents = boxes[box_number]
        matches = [i for i, (l, _) in enumerate(contents) if label == l]
        if matches:
            contents[matches[0]] = (label, int(number))
        else:
            contents.append((label, int(number)))

total = 0
for box_number, contents in enumerate(boxes.values(), 1):
    total += focusing_power(box_number, contents)

print("Part 2:", total)
