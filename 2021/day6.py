import re
def countDown(num):
	num -= 1
	if num < 0:
		num = 6
	return num

def countDownList(li):
	return list(map(countDown, li))

def addNewFish(li):
	n = li.count(0)
	for x in range(0, n):
		li.append(9)
	return li

def day(li):
	li = addNewFish(li)
	li = countDownList(li)
	return li

mylist = []
file = open("day6.txt")
for row in file:
	numbers = re.findall("\d+", row)
	numbers = map(lambda x: int(x), numbers)
	mylist.extend(numbers)

for n in range(0, 80):
	mylist = day(mylist)

print("Part 1: "+str(len(mylist)))