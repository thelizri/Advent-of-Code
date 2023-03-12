#Part 1
file = open("day1.txt", "r")
previous = int(file.readline())
counter = 0

for row in file:
	if previous<int(row):
		counter += 1
	previous = int(row)

print("Part 1: " + str(counter))

#Part 2
file.seek(0)
a = int(file.readline())
b = int(file.readline())
c = int(file.readline())
counter = 0
for row in file:
	prev = a + b + c
	current = b + c + int(row)
	if prev < current:
		counter += 1
	a, b, c = b, c, int(row)

print("Part 2: " + str(counter))

file.close()