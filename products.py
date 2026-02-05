products = {} 
for i in range(3): 

    name = input("Enter the product name: ") 

    quantity = int(input("Enter the quantity: ")) 

    products[name] = quantity 

print(f"Products: {products}") 
