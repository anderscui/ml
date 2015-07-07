from pandas import Series, DataFrame
import numpy as np
import pandas as pd

# Series
obj = Series(np.arange(4.), index=['a', 'b', 'c', 'd'])
print(obj['b'])
print(obj[['b', 'a', 'd']])
print(obj[1])
print(obj[2:4])

print(obj[[1, 3]])
print(obj[obj < 2])

print(obj['b':'c'])
obj['b':'c'] = 5

# DataFrame
data = DataFrame(np.arange(16).reshape((4, 4)),
                 index=['Ohio', 'Colorado', 'Utah', 'New York'],
                 columns=['one', 'two', 'three', 'four'])
print(data)

# rows
print(data[:2])
print(data[data['three'] > 6])

# rows and cols
print(data.ix['Colorado', ['two', 'three']])
print(data.ix[['Colorado', 'Utah'], [3, 0, 1]])

print(data.ix[:'Utah', 'two'])

print(data.ix[data.three > 5, :3])