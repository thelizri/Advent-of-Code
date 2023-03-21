file = open("day14.txt", "r")
file.seek(0)

li = file.readline().strip()
print(li)

file.readline()
for row in file:
	t = row.strip().split(" -> ")
	print(t)
