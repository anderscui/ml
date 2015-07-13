import numpy as np

arr = np.arange(15).reshape((3, 5))
print(arr.T)
print(arr.transpose())

print(np.dot(arr.T, arr))

# also swapaxes()

