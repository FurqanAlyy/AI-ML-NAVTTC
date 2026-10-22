import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

print(arr[:4])

print(arr[1:3:2])

arr1 = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

print(arr1[1, 2:6])
print(arr1[0:2, 3:4])