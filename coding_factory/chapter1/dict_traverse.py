products = {1:"apples", 2:"bananas", 3:"pears"}

for key in products.keys():
    print(key)

for key in products.keys():
    print(key, products[key])    

for value in products.values():
    print(value)    

for key, value in products.items():
    print(key,value)    