import re

text = """Time:      7  15   30
Distance:  9  40  200""".splitlines()

# text = open("day6.txt").read().splitlines()

pattern = re.compile(r"\d+")
times = [int(number) for number in re.findall(pattern, text[0])]
distances = [int(number) for number in re.findall(pattern, text[1])]

print(distances)
