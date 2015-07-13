from pandas import Series, DataFrame
import numpy as np
import pandas as pd

s1 = Series([7.3, -2.5, 3.4, 1.5], index=['a', 'c', 'd', 'e'])
s2 = Series([-2.1, 3.6, -1.5, 4, 3.1], index=['a', 'c', 'e', 'f', 'g'])
print(s1 + s2)

df1 = DataFrame(np.arange(12.).reshape((3, 4)), columns=list('abcd'))
df2 = DataFrame(np.arange(20.).reshape((4, 5)), columns=list('abcde'))
print(df1)
print('')
print(df2)

print('without fill value')
print(df1.add(df2))

print('with fill value')
print(df1.add(df2, fill_value=0))

# set fill value when reindexing
print(df1.reindex(columns=df2.columns, fill_value=0))

