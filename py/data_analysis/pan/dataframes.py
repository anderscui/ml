from pandas import Series, DataFrame
import numpy as np
import pandas as pd

data = {'state': ['Ohio', 'Ohio', 'Ohio', 'Nevada', 'Nevada'],
        'year': [2000, 2001, 2002, 2001, 2002],
        'pop': [1.5, 1.7, 3.6, 2.4, 2.9]}
frame = DataFrame(data)
frame2 = DataFrame(data, columns=['year', 'state', 'pop'])
print(frame)
print(frame2)

# specified columns and indices
frame3 = DataFrame(data, columns=['year', 'state', 'pop', 'debt'],
                   index=['one', 'two', 'three', 'four', 'five'])
print(frame3)

# access a column
print(frame3['state'])
print(frame3.year)

frame3['debt'] = 16.5

# access a row
print(frame3.ix['three'])

# a new col
frame3['eastern'] = frame3.state == 'Ohio'
print(frame3)

# delete a col
del frame3['eastern']
print(frame3.columns)

# nested dict
pop = {'Nevada': {2001: 2.4, 2002: 2.9 },
       'Ohio': {2000: 1.5, 2001: 1.7, 2002: 3.6}}
frame4 = DataFrame(pop)
print(frame4)

# transpose
print(frame4.T)