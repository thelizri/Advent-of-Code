import re
def countDown(tu):
	[num, amount] = tu
	num -= 1
	if num < 0:
		num = 6
	return [num, amount]

def countDownList(li):
	return list(map(countDown, li))

def findNumber(li, num):
	[timer, amount] = li
	return timer == num

def addNewFish(li):
	ll = list(filter(lambda x: findNumber(x, 0), li))
	if ll == []:
		return li
	else:
		[[timer, amount]] = ll
		li.append([9, amount])
		return li

def mergeSixes(li):
	allSixes = list(filter(lambda x: findNumber(x, 6), li))
	count = 0
	for x in allSixes:
		[timer, amount] = x
		count += amount
		li.remove(x)
	li.append([6, count])
	return li

def day(li):
	li = addNewFish(li)
	li = mergeSixes(li)
	li = countDownList(li)
	return li

def countFish(li):
	fish = 0
	for x in li:
		[timer, amount] = x
		fish += amount
	return fish

def reformat(li):
	result = []
	for n in range(0, 7):
		count = li.count(n)
		if count == 0: continue
		result.append([n, li.count(n)])
	return result

mylist = []
file = open("day6.txt")
for row in file:
	numbers = re.findall("\d+", row)
	numbers = map(lambda x: int(x), numbers)
	mylist.extend(numbers)

mylist = reformat(mylist)

for i in range(0, 80):
	mylist = day(mylist)

fish = countFish(mylist)
print("Part 1: "+str(fish))

for i in range(80, 256):
	mylist = day(mylist)

fish = countFish(mylist)
print("Part 2: "+str(fish))

file.close()