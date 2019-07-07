products = []
while True:
	name = input('Please enter the product name:')
	if name == 'q':
		break
	price = input('Please enter the product price')
	products.append([name, price])
print(products)

for p in products:
	print('The price of', p[0], 'is' ,p[1], '.' )

with open('products.csv', 'w', encoding = 'utf-8 ') as f:
		for p in products:
			f.write(p[0] + ',' + p[1] + '\n')