import numpy as np

arr = np.empty((8, 4))
for i in range(8):
    arr[i] = i

print(arr)
print(arr[1])
print(arr[1, :])
print(arr[[4, 3, 0, 6]])

print('---')
arr = np.arange(32).reshape((8, 4))
print(arr[[1, 5, 7, 2], [0, 3, 1, 2]])
print(arr[[1, 5, 7, 2]][:, [0, 3, 1, 2]])
print(arr[np.ix_([1, 5, 7, 2], [0, 3, 1, 2])])