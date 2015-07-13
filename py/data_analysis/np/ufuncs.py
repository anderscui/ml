import numpy as np

arr = np.arange(10)
print(np.exp(arr))

from numpy.random import randn
x = randn(8)
y = randn(8)

print(np.maximum(x, y))

# may returns multiple arrays
arr = randn(7) * 5
print(np.modf(arr))
print(np.modf(-1.23))