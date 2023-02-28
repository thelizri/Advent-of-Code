prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97] #First 25 prime numbers
products = [9059606, 44676511, 2310, 2800733, 95041567, 907383479, 4132280413, 3118414, 8795307, 19720385, 41281849, 103256791]
#Diagonal top-left to bottom-right, Diagonal bottom-left to top-right, row 0-4, col 0-4

product = 1
for i in range(0, 25, 6):
	product *= prime[i]
products.append(product)

product = 1
for i in range(4, 21, 4):
	product *= prime[i]
products.append(product)

for row in range(0, 5):
	product = 1
	for i in range(0, 5):
		product *= prime[i+row*5]
	products.append(product)

for col in range(0, 5):
	product = 1
	for i in range(0, 5):
		product *= prime[col + i*5]
	products.append(product)

print(products)