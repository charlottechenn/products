products = []
while True:
    name = input('請輸入商品名稱：')
    if name == 'q': #quit
    	break
    price = input('請輸入商品價格：')
    p = [name,price]
    products.append(p)
print(products)

products[0][0]