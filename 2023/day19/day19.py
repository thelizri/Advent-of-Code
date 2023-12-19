# Parsing the given text which seems to be a set of rules or conditions in a specific format

# The given text
text = """
px{a<2006:qkq,m>2090:A,rfg}
pv{a>1716:R,A}
lnx{m>1548:A,A}
rfg{s<537:gd,x>2440:R,A}
qs{s>3448:A,lnx}
qkq{x<1416:A,crn}
crn{x>2662:A,R}
in{s<1351:px,qqz}
qqz{s>2770:qs,m<1801:hdj,R}
gd{a>3333:R,R}
hdj{m>838:A,pv}

{x=787,m=2655,a=1222,s=2876}
{x=1679,m=44,a=2067,s=496}
{x=2036,m=264,a=79,s=2244}
{x=2461,m=1339,a=466,s=291}
{x=2127,m=1623,a=2188,s=1013}
"""

text = open("day19.txt").read()

rules_text, dictionaries_text = text.split("\n\n")


def parse_rules(text):
    # Splitting the text into lines and parsing each line
    rules = {}
    for line in text.strip().splitlines():
        key, conditions = line.split("{")
        conditions = conditions[:-1]  # Remove the closing brace
        rules[key] = []

        # Splitting conditions and parsing each condition
        for condition in conditions.split(","):
            if ":" in condition:
                condition_parts = condition.split(":")
                condition_detail = condition_parts[0]
                destination = condition_parts[1]
            else:
                condition_detail = None
                destination = condition

            # Parsing the condition detail (e.g., "a<2006")
            if condition_detail is not None and "<" in condition_detail:
                condition_type, condition_value = condition_detail.split("<")
                condition_value = int(condition_value)
                comparison = "<"
            elif condition_detail is not None and ">" in condition_detail:
                condition_type, condition_value = condition_detail.split(">")
                condition_value = int(condition_value)
                comparison = ">"
            else:
                # No comparison operator found
                condition_type = None
                condition_value = None
                comparison = None

            # Adding parsed condition to the rule
            rules[key].append(
                {
                    "type": condition_type,
                    "value": condition_value,
                    "comparison": comparison,
                    "targets": destination,
                }
            )
    return rules


def parse_dictionaries(text):
    records = []
    for line in text.strip().splitlines():
        # Remove the curly braces and split by comma
        elements = line[1:-1].split(",")
        record = {}

        # Splitting each element by '=' and adding to the dictionary
        for element in elements:
            key, value = element.split("=")
            record[key] = int(value)

        records.append(record)

    return records


def get_accepted():
    rules = parse_rules(rules_text)
    dictionaries = parse_dictionaries(dictionaries_text)
    accepted = []

    operators = {
        ">": int.__gt__,
        "<": int.__lt__,
    }

    for dictionary in dictionaries:
        rule = rules["in"]
        while rule is not None:
            for condition in rule:
                passed = False
                if condition["comparison"] is not None:
                    op = operators[condition["comparison"]]
                    if op(dictionary[condition["type"]], condition["value"]):
                        passed = True
                else:
                    passed = True

                if passed:
                    target = condition["targets"]
                    if target == "R":
                        rule = None
                    elif target == "A":
                        accepted.append(dictionary)
                        rule = None
                    else:
                        rule = rules[target]
                    break
    return accepted


def part1():
    total = 0
    for accepted in get_accepted():
        for value in accepted.values():
            total += value
    return total


print("Part 1:", part1())
