products = []
while True:
    name = input('請輸入商品名稱: ')
    if name == 'q':
        break
    price = input('請輸入商品價格: ')  
    products.append([name, price]) 
print(products)

products[0][0]                 #存取清單?


#products.append([name, price])
    #p = [name, price]
    #products.append(p)
        #p = []
        #p.append(name)
        #p.append(price)