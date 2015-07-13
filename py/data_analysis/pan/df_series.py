from pandas import Series, DataFrame
import numpy as np
import pandas as pd

arr = np.arange(12.).reshape((3, 4))
print(arr)
print(arr[0])
print(arr - arr[0])