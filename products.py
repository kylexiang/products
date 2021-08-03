products = [];
while True:
	name = input("请输入产品名称：");
	if name == 'q':
		break
	price  = input("请输入产品价格：");
	products.append([name,price]);

for product in products:
	print(products[0][0], '价格是', products[0][1]);
