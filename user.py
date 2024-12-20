"""User nomli Named tuple yarating """
from collections import namedtuple
from traceback import print_tb

User = namedtuple('User', ['name', 'age', 'email', 'job'], defaults=[None, None, 0, None])

ali = User('ali', 30, 'ali@gmail.com', 'driver')

print(ali)
print(ali.name)
print(ali.age)
print(ali.email)
print(ali.job)

vali = User()   # u default holatda
print(vali)
