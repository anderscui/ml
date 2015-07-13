import numpy as np

# creating
data1 = [6, 7.5, 8, 0, 1]
arr1 = np.array(data1)
print(arr1)
print(arr1.dtype)  # float64

data2 = [[1, 2, 3, 4], [5, 6, 7, 8]]
arr2 = np.array(data2)
print(arr2, arr2.ndim, arr2.shape)
print(arr2.dtype)  # int64

print(np.zeros(10))
print(np.ones((3, 5)))
print(np.empty((2, 3, 2)))
print(np.eye(5))

print(np.arange(6))

# explicit dtype
arr3 = np.array([1, 2, 3], dtype=np.float64)
print(arr3)

# casting
arr4 = np.array([xrange(6)])
print(arr4.dtype)
arr4_f = arr4.astype(np.float64)
print(arr4_f.dtype)

num_str = np.array(['1.25', '-9.6', '42'])
num_arr = num_str.astype(float)
print(num_arr.dtype)

# type shorthands
empty_uint32 = np.empty(8, dtype='u4')
print(empty_uint32, empty_uint32.dtype)




