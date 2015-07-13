import numpy as np
from numpy.random import randn

names = np.array(['Bob', 'Joe', 'Will', 'Bob', 'Will', 'Joe', 'Joe'])
data = randn(7, 4)
print(names)
print(data)

print(names == 'Bob')
print(data[names == 'Bob'])
print(data[names == 'Bob', 2:])

print(data[names != 'Bob'])
print(data[-(names == 'Bob')])

mask = (names == 'Bob') | (names == 'Will')
print(data[mask])

data[data < 0] = 0
print(data)