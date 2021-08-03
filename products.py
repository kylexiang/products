products = [];
while True:
	name = input("请输入产品名称：");
	if name == 'q':
		break
	price  = input("请输入产品价格：");
	products.append([name,price]);
print(products);
