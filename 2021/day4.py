import re

prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] #First 25 prime numbers
products = [9059606, 44676511, 2310, 2800733, 95041567, 907383479, 4132280413, 3118414, 8795307, 19720385, 41281849, 103256791]
#Diagonal top-left to bottom-right, Diagonal bottom-left to top-right, row 0-4, col 0-4

file = open("day4.txt")
bingo_numbers = file.readline().strip().split(",")
bingo_numbers = list(map(lambda x: int(x), bingo_numbers))

rows = list(map(lambda x: x.strip(), file.readlines()))
rows = list(filter(lambda x: x, rows))

i = 0
bingo_boards = []
while i < len(rows)/5:
	board = []
	for j in range(0,5):
		row = rows[j+i*5]
		nums = list(map(lambda x: int(x), re.findall("\d+", row)))
		for num in nums: board.append(num)
	bingo_boards.append(board)
	i += 1

