import numpy as np

x = np.array([3, 1, 2])
print(np.argsort(x))

k = 2
print(np.argsort(x)[::-1][:k])