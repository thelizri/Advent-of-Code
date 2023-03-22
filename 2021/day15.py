import re

#Goal: Find path with lowest total risk

#Read input
file = open("day15.txt", "r")

matrix = []
for row in file:
	row.strip()
	line = list(row)
	matrix.append(line)

print(matrix)