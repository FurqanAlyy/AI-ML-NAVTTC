import pandas as pd

# Example 1
df = pd.read_csv('data.csv')
print(df.to_string())

# Example 2
print(df)

# Example 3
print(pd.options.display.max_rows)

# Example 4
pd.options.display.max_rows = 9999
print(df)
