from collections import Counter

#Reading input
file = open("day14.txt", "r")
file.seek(0)

string = file.readline().strip()
li = [s for s in string]
table = dict()

file.readline()
for row in file:
	[pair, insert] = row.strip().split(" -> ")
	[a, b] = pair
	key = (a, b)
	table[key] = insert

#Part 1
def part1(table, li):
	copy = li.copy()
	length = len(li)
	modifier = 0
	for index in range(1, length):
		a = li[index-1]
		b = li[index]
		key = (a, b)
		value = table.get(key)
		if value:
			copy.insert(index+modifier, value)
			modifier += 1
	return copy

def mostAndLeastCommonElement(li):
	counter = Counter(li)
	count_list = list(counter.most_common())
	most = count_list[0][1]
	least = count_list[-1][1]
	return most - least

for i in range(10):
	li = part1(table, li)

result = mostAndLeastCommonElement(li)
print("Part 1: "+str(result))

#Part 2
# for i in range(30):
# 	print(i)
# 	li = part1(table, li)
# 	print(mostAndLeastCommonElement(li))

# result = mostAndLeastCommonElement(li)
# print("Part 2: "+str(result))