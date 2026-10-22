import pandas as pd

records = pd.DataFrame({
    "Duration": [30, 45, 450, 60, 60],
    "Date": ["2026/01/01", "bad date", "2026/01/03", "2026/01/04", "2026/01/04"],
    "Pulse": [95, 110, 105, 100, 100],
    "Calories": [180.0, None, 290.0, 320.0, 320.0],
})
print("Before cleaning:")
print(records)

print("Rows without missing values:")
print(records.dropna())
records["Calories"] = records["Calories"].fillna(records["Calories"].mean())

records["Date"] = pd.to_datetime(records["Date"], format="%Y/%m/%d", errors="coerce")
records = records.dropna(subset=["Date"]).copy()

records.loc[records["Duration"] > 120, "Duration"] = 45

print("Duplicate flags:")
print(records.duplicated())
records = records.drop_duplicates()
print("After cleaning:")
print(records)
