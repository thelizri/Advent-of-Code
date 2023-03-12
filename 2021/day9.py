file = open("day9.txt", "r")
file.seek(0)

#Lets convert the input to a matrix
result = []
for row in file:
	numbers = []
	for digit in row.strip():
		if digit.isdigit(): numbers.append(int(digit))
	result.append(numbers)

file.close()
height = len(result)
width = len(result[0])

def valid_coord(x, y):
	if x >= 0 and x < width:
		if y >= 0 and y < height:
			return True
	return False

def is_low_point(x, y):
	value = result[y][x]

	#Check up
	if valid_coord(x, y-1):
		adj = result[y-1][x]
		if adj <= value: return False

	#Check down
	if valid_coord(x, y+1):
		adj = result[y+1][x]
		if adj <= value: return False

	#Check right
	if valid_coord(x+1, y):
		adj = result[y][x+1]
		if adj <= value: return False

	#Check left
	if valid_coord(x-1, y):
		adj = result[y][x-1]
		if adj <= value: return False

	return True

sum = 0
for y in range(0, height):
	for x in range(0, width):
		if is_low_point(x, y):
			sum += (1+result[y][x])

print("Part 1: "+str(sum))
