import pandas as pd

# Example 1
a = [1, 7, 2]
myvar = pd.Series(a)
print(myvar)

# Example 2
print(myvar[0])

# Example 3
myvar = pd.Series(a, index = ["x", "y", "z"])
print(myvar)

# Example 4
print(myvar["y"])

# Example 5
calories = {"day1": 420, "day2": 380, "day3": 390}
myvar = pd.Series(calories)
print(myvar)

# Example 6
myvar = pd.Series(calories, index = ["day1", "day2"])
print(myvar)

# Example 7
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}
myvar = pd.DataFrame(data)
print(myvar)
