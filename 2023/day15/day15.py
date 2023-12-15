def hash_label(label):
    """Compute the custom hash of a label."""
    current_value = 0
    for ch in label:
        current_value = (current_value + ord(ch)) * 17 % 256
    return current_value


def calculate_total_amount(instructions):
    """Calculate the total amount as per Part 1."""
    return sum(hash_label(instruction) for instruction in instructions)


def focusing_power(box_number, contents):
    """Calculate the focusing power for a box."""
    return sum(
        box_number * slot_number * focal_length
        for slot_number, (_, focal_length) in enumerate(contents, 1)
    )


def process_instructions(instructions):
    """Process instructions to get the total focusing power as per Part 2."""
    boxes = {i: [] for i in range(256)}

    for instruction in instructions:
        if "-" in instruction:
            label = instruction[:-1]
            box_number = hash_label(label)
            boxes[box_number] = [(l, f) for l, f in boxes[box_number] if l != label]
        else:
            label, number = instruction.split("=")
            box_number = hash_label(label)
            contents = boxes[box_number]
            matches = [i for i, (l, _) in enumerate(contents) if l == label]
            if matches:
                contents[matches[0]] = (label, int(number))
            else:
                contents.append((label, int(number)))

    return sum(
        focusing_power(box_number + 1, contents)
        for box_number, contents in boxes.items()
    )


# Example usage
input_data = "rn=1,cm-,qp=3,cm=2,qp-,pc=4,ot=9,ab=5,pc-,pc=6,ot=7".split(",")

# Real data
input_data = open("day15.txt").read().split(",")

print("Part 1:", calculate_total_amount(input_data))
print("Part 2:", process_instructions(input_data))
