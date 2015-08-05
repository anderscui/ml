import numpy as np
import matplotlib.pyplot as plt

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr)
print(arr[:, :])

inds = np.array([0, 1])
print(arr[:, inds])

row1 = arr[0, :]
print(row1)
inds2 = [2, 1]
print(row1[inds2])