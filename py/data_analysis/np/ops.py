import numpy as np

arr = np.array([[1., 2., 3.], [4., 5., 6.]])
print(arr)
print(arr + arr)
print(arr * arr)

print(1/arr)
print(arr ** 0.5)

# indexing and slicing
arr2 = np.arange(10)
print(arr2)
arr2[5:8] = 12
print(arr2)

# view
arr2_slice = arr2[5:8]
arr2_slice[1] = 12345
print(arr2)
arr2_slice[:] = 64
print(arr2)

## 2d array
arr2d = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
print(arr2d[2])

print(arr2d[0][2], arr2d[0, 2])
print(arr2d[:2])
print(arr2d[:2, 1:])  # 2x2

## 3d array
arr3d = np.array([[[1, 2, 3], [4, 5, 6]],
                  [[7, 8, 9], [10, 11, 12]]])
print(arr3d[0])

old_vals = arr3d[0].copy()
print(old_vals)

# update val
arr3d[0] = 42
print(arr3d[0])

arr3d[0] = old_vals
print(arr3d[0])


