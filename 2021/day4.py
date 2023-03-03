import re
# Step 1: Parse input and create bingo boards
# Step 2: All bingo boards start with state 1.
# Step 3: Draw next number. Check if any bingo boards contain number.
# Step 4: If they do. Take the index, get the prime at that index, and multiply the state with it.
# Step 5: Check if any of the boards has bingo. If they do, calculate the score.

bingo_boards = []
bingo_states = []
prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] #First 25 prime numbers
products = [2310, 2800733, 95041567, 907383479, 4132280413, 3118414, 8795307, 19720385, 41281849, 103256791] # We can use these numbers to check if a bingo board has won
#Diagonal top-left to bottom-right, Diagonal bottom-left to top-right, row 0-4, col 0-4

def checkIfBoardHasWon(board_state):
	for i in products:
		if board_state % i == 0:
			return True
	return False

def addBingoNumberToAllBoards(number):
	for i in range(0, len(bingo_boards)):
		if number in bingo_boards[i]: #Check for number in board
			index = bingo_boards[i].index(number)
			bingo_states[i] *= prime[index] #This is wrong. Should be the index of match

def getWinningBoard():
	for i in range(0, len(bingo_states)):
		if bingo_states[i] == 0: continue
		if checkIfBoardHasWon(bingo_states[i]):
			return i
	return -1

#Sum of all unmarked number
def calcScoreOfBoard(indexOfBoard, bingo):
	board = bingo_boards[indexOfBoard]
	state = bingo_states[indexOfBoard]
	thesum = 0
	for i in range(0, len(prime)):
		p = prime[i]
		if state % p == 0:
			continue
		else:
			thesum += board[i]
	return thesum*bingo

file = open("day4.txt")
bingo_numbers = file.readline().strip().split(",")
bingo_numbers = list(map(lambda x: int(x), bingo_numbers))

rows = list(map(lambda x: x.strip(), file.readlines()))
rows = list(filter(lambda x: x, rows))

#Init bingo boards
i = 0
while i < len(rows)/5:
	board = []
	for j in range(0,5):
		row = rows[j+i*5]
		nums = list(map(lambda x: int(x), re.findall("\d+", row)))
		for num in nums: board.append(num)
	bingo_boards.append(board)
	i += 1

#Init states
for i in bingo_boards:
	bingo_states.append(1)

#Draw bingo numbers
for bingo in bingo_numbers:
	addBingoNumberToAllBoards(bingo)
	result = getWinningBoard()
	if result != -1:
		print("Part 1: "+str(calcScoreOfBoard(result, bingo)))
		break

#Part 2

def getWinningBoardPart2():
	result = []
	for i in range(0, len(bingo_states)):
		if bingo_states[i] == 0: continue
		if checkIfBoardHasWon(bingo_states[i]):
			result.append(i)
	return result

def calcScoreOfBoardPart2(indexOfBoard, bingo):
	board = bingo_boards[indexOfBoard]
	thesum = 0
	for i in bingo_numbers:
		if i == bingo: board.remove(i); break
		if i in board: board.remove(i)
	return sum(board)*bingo

#Init states again
bingo_states = []
for i in bingo_boards:
	bingo_states.append(1)

#Draw bingo numbers again
last = -1
lastb = -1
for bingo in bingo_numbers:
	addBingoNumberToAllBoards(bingo)
	result = getWinningBoardPart2()
	if result != []:
		if len(result) == 1:
			last = result[0]
			lastb = bingo
			bingo_states[last]=0
		else:
			for i in result:
				bingo_states[i]=0

print("Part 2: "+str(calcScoreOfBoardPart2(last, lastb)))
