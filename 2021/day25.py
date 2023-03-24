#Reading input
file = open("day25.txt", "r")
file.seek(0)

matrix = []
for row in file:
	line = []
	for character in row.strip():
		if character == ">":
			line.append(1)
		elif character == "v":
			line.append(-1)
		else: line.append(0)
	matrix.append(line)

#1 represents rightwards direction
#-1 represents downwards direction

height = len(matrix)
width = len(matrix[0])
