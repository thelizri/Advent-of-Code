input = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".splitlines()


def count(arrangement, condition):
    if not arrangement:
        if not condition:
            return 1
        else:
            return 0
    if not condition:
        if "#" in arrangement:
            return 0
        else:
            return 1

    result = 0
    if arrangement[0] in ".?":
        (num, *rest) = condition
        if num == 0:
            result += count(arrangement[1:], condition[1:])
        else:
            result += count(arrangement[1:], condition)

    if arrangement[0] in "#?":
        (num, *rest) = condition
        if num > 0:
            result += count(arrangement[1:], (num - 1, *rest))

    return result


def part1():
    total = 0
    for row in input:
        record, condition = row.split(" ")
        condition = tuple([int(number) for number in condition.split(",")])
        c = count(record, condition)
        print(c)
        total += c

    print("Part 1:", total)


part1()
