import re
import numpy as np

text = """Time:      7  15   30
Distance:  9  40  200""".splitlines()

text = open("day6.txt").read().splitlines()

pattern = re.compile(r"\d+")
times = [int(number) for number in re.findall(pattern, text[0])]
distances = [int(number) for number in re.findall(pattern, text[1])]

# 0 m/s starting speed
# 1 m/s^2 acceleration
# the boat can't move until you let go of the button
# number of ways to beat the record in each race


def distance_travelled(time_holding_button, time_of_race):
    speed = time_holding_button
    distance = (time_of_race - time_holding_button) * speed
    return distance


part1 = []
for time, record in zip(times, distances):
    amount = 0
    for i in range(time):
        distance = distance_travelled(i, time)
        if distance > record:
            amount += 1
    part1.append(amount)

print("Part 1:", np.prod(part1))
