from pandas import Series, DataFrame
import numpy as np
import pandas as pd

obj = Series([4, 7, -5, 3])
print(obj)
print(obj.index)  # default numeric index
print(obj.values)

obj2 = Series([4, 7, -5, 3], index=['d', 'b', 'a', 'c'])
print(obj2)
print(obj2['a'])
obj2['d'] = 6
print(obj2[['c', 'a', 'd']])

# boolean ops
print(obj2)
print(obj2[obj2 > 0])
print(obj2 * 2)
print(np.exp(obj2))

# ordered dict
print('b' in obj2)
print('e' in obj2)

# from dict
sdata = {'Ohio': 35000, 'Texas': 71000, 'Oregon': 16000, 'Utah': 5000}
obj3 = Series(sdata)
print(obj3)

states = ['California', 'Oregon', 'Ohio', 'Texas']
obj4 = Series(sdata, index=states)
print(obj4)

# missing values
print(pd.isnull(obj4))  # or obj4.isnull()
print(pd.notnull(obj4))

# name
obj4.name = 'population'
obj4.index.name = 'state'
print(obj4)

# index assignment
print(obj)
obj.index = ['Bob', 'Steve', 'Jeff', 'Ryan']
print(obj)

