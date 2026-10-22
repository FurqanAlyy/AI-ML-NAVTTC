import numpy as np

# Example 1
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print(arr)

# Example 2
arr1 = np.array([[1, 2], [3, 4]])
arr2 = np.array([[5, 6], [7, 8]])
arr = np.concatenate((arr1, arr2), axis=1)
print(arr)

# Example 3
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.stack((arr1, arr2), axis=1)
print(arr)

# Example 4
arr = np.hstack((arr1, arr2))
print(arr)

# Example 5
arr = np.vstack((arr1, arr2))
print(arr)

# Example 6
arr = np.dstack((arr1, arr2))
print(arr)
