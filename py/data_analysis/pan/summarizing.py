from pandas import Series, DataFrame
import numpy as np
import pandas as pd

df = DataFrame([[1.4, np.nan],
                [7.1, -4.5],
                [np.nan, np.nan],
                [-0.75, -1.3]],
               index=['a', 'b', 'c', 'd'],
               columns=['one', 'two'])
print(df)

# sum by columns
print(df.sum())
# sum by rows
print(df.sum(axis=1))

# skip NA
print(df.mean(axis=1, skipna=False))

# summary
print(df.describe())