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
