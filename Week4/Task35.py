import numpy as np

# Example 1
arr = np.array([1, 2, 3])
for x in arr:
    print(x)

# Example 2
arr = np.array([[1, 2, 3], [4, 5, 6]])
for x in arr:
    print(x)

# Example 3
for x in arr:
    for y in x:
        print(y)

# Example 4
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for x in arr:
    print(x)

# Example 5
for x in arr:
    for y in x:
        for z in y:
            print(z)

# Example 6
arr = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for x in np.nditer(arr):
    print(x)

# Example 7
arr = np.array([1, 2, 3])
for x in np.nditer(arr, flags=['buffered'], op_dtypes=['S']):
    print(x)

# Example 8
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x in np.nditer(arr[:, ::2]):
    print(x)

# Example 9
arr = np.array([1, 2, 3])
for idx, x in np.ndenumerate(arr):
    print(idx, x)

# Example 10
arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for idx, x in np.ndenumerate(arr):
    print(idx, x)
