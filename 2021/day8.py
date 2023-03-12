import re

#Part 1
def test(s):
	if len(s) > 1 and len(s) < 5: return True
	elif len(s) == 7: return True
	else: return False

file = open("day8.txt", "r")
file.seek(0)

sum = 0
for row in file:
	li = row.split("|")
	codes = re.findall("[a-z]+", li[1])
	matches = list(filter(test, codes))
	sum += len(matches)

print("Part 1: "+str(sum))

#Part 2
#Please don't look at this solution. It is some of the ugliest code I've ever written
def create_set(s):
	result = set(())
	for char in s:
		result.add(char)
	return result

def decode(s):
	codes = s.split(" ")
	seven = list(filter(lambda x: len(x)==3, codes))[0]
	seven = create_set(seven)
	one = list(filter(lambda x: len(x)==2, codes))[0]
	one = create_set(one)
	eight = list(filter(lambda x: len(x)==7, codes))[0]
	eight = create_set(eight)
	four = list(filter(lambda x: len(x)==4, codes))[0]
	four = create_set(four)
	li235 = list(filter(lambda x: len(x)==5, codes))
	li069 = list(filter(lambda x: len(x)==6, codes))
	two = findTwo(li235, four)
	five = findFive(li235, two)
	three = findThree(li235, two)
	nine = findNine(li069, four)
	zero = findZero(li069, five)
	six = findSix(li069, seven)

	return [zero, one, two, three, four, five, six, seven, eight, nine]
	
def findTwo(li, four):
	for code in li:
		s = create_set(code)
		if len(s.intersection(four)) == 2:
			return s

def findFive(li, two):
	for code in li:
		s = create_set(code)
		if len(s.intersection(two)) == 3:
			return s

def findThree(li, two):
	for code in li:
		s = create_set(code)
		if len(s.intersection(two)) == 4:
			return s

def findNine(li, four):
	[a, b, c] = li
	a = create_set(a)
	b = create_set(b)
	c = create_set(c)
	result = a.intersection(b).intersection(c)
	result = result.union(four)
	return result

def findZero(li, five):
	for code in li:
		s = create_set(code)
		if len(s.difference(five)) == 2:
			return s

def findSix(li, seven):
	for code in li:
		s = create_set(code)
		if len(s.difference(seven)) == 4:
			return s

def translate(dic, s):
	li = s.strip().split(" ")
	res = ""
	for x in li:
		s = create_set(x)
		if s in dic:
			res += str(dic.index(s))
	return int(res)


file.seek(0)
sum = 0
for row in file:
	[codes, result] = row.split("|")
	dic = decode(codes)
	sum += translate(dic, result)

print("Part 2: "+str(sum))

file.close()