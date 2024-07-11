# products.py
products = []

def add_product(name, price):
    products.append({'name': name, 'price': price})

def list_products():
    return products

def edit_product(index, name, price):
    if 0 <= index < len(products):
        products[index] = {'name': name, 'price': price}

def delete_product(index):
    if 0 <= index < len(products):
        products.pop(index)

# Add some sample products
add_product('T-shirt', 20)
add_product('Jeans', 50)