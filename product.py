"""Product  nomli Named tuple yarating"""
from collections import namedtuple


Product = namedtuple('Product', ['name', 'price', 'quantity'])

product1 = Product(name="Olma", price=5000, quantity=10)


print(product1)

print(product1.name)
print(product1.price)
print(product1.quantity)



