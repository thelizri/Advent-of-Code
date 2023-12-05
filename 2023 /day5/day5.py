import re

text = """seeds: 79 14 55 13

seed-to-soil map:
50 98 2
52 50 48

soil-to-fertilizer map:
0 15 37
37 52 2
39 0 15

fertilizer-to-water map:
49 53 8
0 11 42
42 0 7
57 7 4

water-to-light map:
88 18 7
18 25 70

light-to-temperature map:
45 77 23
81 45 19
68 64 13

temperature-to-humidity map:
0 69 1
1 0 69

humidity-to-location map:
60 56 37
56 93 4
""".split(
    "\n\n"
)

text = open("day5.txt").read().split("\n\n")

# dest range start, source range start, length

# Any source numbers that aren't mapped correspond to the same destination number

pattern = re.compile(r"\d+")
seeds = re.findall(pattern, text[0])
seed_to_soil = re.findall(pattern, text[1])
soil_to_fertilizer = re.findall(pattern, text[2])
fertilizer_to_water = re.findall(pattern, text[3])
water_to_light = re.findall(pattern, text[4])
light_to_temperature = re.findall(pattern, text[5])
temperature_to_humidity = re.findall(pattern, text[6])
humidity_to_location = re.findall(pattern, text[7])

seeds = [int(number) for number in seeds]
seed_to_soil = [int(number) for number in seed_to_soil]
soil_to_fertilizer = [int(number) for number in soil_to_fertilizer]
fertilizer_to_water = [int(number) for number in fertilizer_to_water]
water_to_light = [int(number) for number in water_to_light]
light_to_temperature = [int(number) for number in light_to_temperature]
temperature_to_humidity = [int(number) for number in temperature_to_humidity]
humidity_to_location = [int(number) for number in humidity_to_location]


def translator(number, map):
    for i in range(0, len(map), 3):
        dest_start, source_start, length = map[i], map[i + 1], map[i + 2]
        if number in range(source_start, source_start + length):
            return dest_start + (number - source_start)

    return number


def translate_seed_to_location(seed):
    soil = translator(seed, seed_to_soil)
    fertilizer = translator(soil, soil_to_fertilizer)
    water = translator(fertilizer, fertilizer_to_water)
    light = translator(water, water_to_light)
    temperature = translator(light, light_to_temperature)
    humidity = translator(temperature, temperature_to_humidity)
    location = translator(humidity, humidity_to_location)
    return location


part1 = float("inf")
for seed in seeds:
    location = translate_seed_to_location(seed)
    part1 = min(part1, location)

print("Part 1:", part1)
