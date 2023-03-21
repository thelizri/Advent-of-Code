file = open("day14.txt", "r")
file.seek(0)

li = file.readline().strip()
print(li)

table = dict()

file.readline()
for row in file:
	[pair, insert] = row.strip().split(" -> ")
	[a, b] = pair
	key = (a, b)
	table[key] = insert


print(table)
