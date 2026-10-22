import pandas as pd

# Example 1
df = pd.read_csv('data.csv')
print(df.head(10))

# Example 2
print(df.head())

# Example 3
print(df.tail())

# Example 4
print(df.info())
