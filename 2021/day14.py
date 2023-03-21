from collections import Counter

#Reading input
file = open("day14.txt", "r")
file.seek(0)

string = file.readline().strip()
di = dict()
for i in range(1,len(string)):
	a = string[i-1]
	b = string[i]
	key = (a, b)
	value = di.get(key, 0)
	di.update({key: value+1})

table = dict()
file.readline()
for row in file:
	[pair, insert] = row.strip().split(" -> ")
	[a, b] = pair
	key = (a, b)
	table[key] = insert

#Methods
def insertLetterInsidePair(table, di):
	copy = di.copy()
	for pair in di.copy().keys():
		insert = table.get(pair)
		if insert:
			v = copy.get(pair)
			t = di.get(pair)
			if t-v==0: di.pop(pair)
			else: di.update({pair: t-v})
			(a, b) = pair
			key = (a, insert)
			value = di.get(key, 0)
			di.update({key: value+v})
			key = (insert, b)
			value = di.get(key, 0)
			di.update({key: value+v})

def convertDictToListOfValues(di):
	temp = dict()
	for pair in di:
		(a, b) = pair
		value = di.get(pair, 0)
		valueInTemp = temp.get(a, 0)
		temp.update({a: value+valueInTemp})
		valueInTemp = temp.get(b, 0)
		temp.update({b: value+valueInTemp})
	return [round(num/2) for num in list(temp.values())]
	return list(temp.values())

#Part 1
for i in range(10):
	insertLetterInsidePair(table, di)

li = convertDictToListOfValues(di)
li.sort()
most = li[-1]
least = li[0]
answer = most - least + 1
print(f"Part 1: {answer}")

#Part 2
for i in range(30):
	insertLetterInsidePair(table, di)

li = convertDictToListOfValues(di)
li.sort()
most = li[-1]
least = li[0]
answer = most - least + 1
print(f"Part 2: {answer}")