import numpy as np

arr1 = np.array([1, 2, 3, 4, 5])
print(arr1)
print(type(arr1))

arr2 = np.array([[1, 2, 3], [4, 5, 6]])
print(arr2)
print(type(arr2))

arr3 = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr3)

arr = np.array([1, 2, 3, 4], ndmin=5)
print(arr)
print('number of dimensions :', arr.ndim)