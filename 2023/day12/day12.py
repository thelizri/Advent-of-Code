from functools import lru_cache

input = """???.### 1,1,3
.??..??...?##. 1,1,3
?#?#?#?#?#?#?#? 1,3,1,6
????.#...#... 4,1,1
????.######..#####. 1,6,5
?###???????? 3,2,1""".splitlines()

input = open("day12.txt").read().splitlines()


@lru_cache(maxsize=None)
def count(arrangement, condition, contiguous=False):
    if not arrangement:
        if not condition:
            return 1
        elif len(condition) == 1 and condition[0] == 0:
            return 1
        else:
            return 0
    if not condition:
        if "#" in arrangement:
            return 0
        else:
            return 1

    (num, *rest) = condition
    result = 0
    if arrangement[0] in ".?" and not contiguous:
        if num == 0:
            result += count(arrangement[1:], condition[1:])
        else:
            result += count(arrangement[1:], condition)

    if arrangement[0] in "#?":
        if num > 1:
            result += count(arrangement[1:], (num - 1, *rest), True)
        elif num == 1:
            result += count(arrangement[1:], (num - 1, *rest))

    return result


def part1():
    total = 0
    for row in input:
        record, condition = row.split(" ")
        condition = tuple([int(number) for number in condition.split(",")])
        total += count(record, condition)

    print("Part 1:", total)


def part2():
    total = 0
    for row in input:
        record, condition = row.split(" ")
        condition = tuple([int(number) for number in condition.split(",")])
        total += count((record + "?") * 4 + record, condition * 5)

    print("Part 2:", total)


part1()
part2()
