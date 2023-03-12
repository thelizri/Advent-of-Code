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

#Part 2
# Use tuples to store coordinates (x, y)
# list.pop for stack
# keep track of score and visited

def basin_size(score, visited, stack, x, y):
	value = result[y][x]
	visited.append((x,y))

	#Check up
	if valid_coord(x, y-1):
		adj = result[y-1][x]
		if adj > value and adj != 9:
			if (x, y-1) not in visited and (x, y-1) not in stack:
				score += 1
				stack.append((x, y-1))

	#Check down
	if valid_coord(x, y+1):
		adj = result[y+1][x]
		if adj > value and adj != 9:
			if (x, y+1) not in visited and (x, y+1) not in stack:
				score += 1
				stack.append((x, y+1))

	#Check right
	if valid_coord(x+1, y):
		adj = result[y][x+1]
		if adj > value and adj != 9:
			if (x+1, y) not in visited and (x+1, y) not in stack:
				score += 1
				stack.append((x+1, y))

	#Check left
	if valid_coord(x-1, y):
		adj = result[y][x-1]
		if adj > value and adj != 9:
			if (x-1, y) not in visited and (x-1, y) not in stack:
				score += 1
				stack.append((x-1, y))

	if len(stack) == 0: return score
	else: 
		(x,y)=stack.pop()
		return basin_size(score, visited, stack, x, y)

li = []
for y in range(0, height):
	for x in range(0, width):
		if is_low_point(x, y):
			li.append(basin_size(1, [], [], x, y))

li.sort(reverse=True)
part2_result = li[0]*li[1]*li[2]
print("Part 2: "+str(part2_result))


