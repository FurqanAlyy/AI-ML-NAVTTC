import pandas as pd

# Example 1
data = {
  "calories": [420, 380, 390],
  "duration": [50, 40, 45]
}

df = pd.DataFrame(data)
print(df)

# Example 2
print(df.loc[0])

# Example 3
print(df.loc[[0, 1]])

# Example 4
df = pd.DataFrame(data, index = ["day1", "day2", "day3"])
print(df)

# Example 5
print(df.loc["day2"])

# Example 6
df = pd.read_csv('data.csv')
print(df)
