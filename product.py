import os
products = []
# Read files
if os.path.isfile('product.csv')
	print('File is here!!!!')
	with open('products.csv', 'r', encoding = 'utf-8 ') as f:
		for line in f:
			if 'Product,Price' in line:
				continue
			name, price = line.strip().split(',')
			products.append([name, price])
	print(products)
else:
	print('Where is the file???')

#Input
while True:
	name = input('Please enter the product name:')
	if name == 'q':
		break
	price = input('Please enter the product price')
	products.append([name, price])
print(products)

#Print all the records
for p in products:
	print('The price of', p[0], 'is' ,p[1], '.' )

#Write to files
with open('products.csv', 'w', encoding = 'utf-8 ') as f:
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')