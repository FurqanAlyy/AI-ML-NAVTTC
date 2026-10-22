import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

rng = np.random.default_rng(55)
dates = pd.date_range("2023-01-01", "2025-12-31", freq="D")
steps = np.arange(len(dates))
energy = pd.DataFrame({
    "Consumption": 100 + 0.01 * steps + 15 * np.cos(2 * np.pi * steps / 365.25)
                   + 5 * np.cos(2 * np.pi * steps / 7) + rng.normal(0, 2, len(dates)),
    "Solar": 20 - 12 * np.cos(2 * np.pi * steps / 365.25),
    "Wind": rng.uniform(5, 30, len(dates)),
}, index=dates)
energy.index.name = "Date"
energy["Renewables"] = energy["Solar"] + energy["Wind"]
print(pd.to_datetime("2025-01-15 15:45"))
print(pd.to_datetime("08/07/2025", dayfirst=True))
print(energy.head())
print(energy.index)

energy["Year"] = energy.index.year
energy["Month"] = energy.index.month
energy["Weekday"] = energy.index.day_name()
print(energy.loc["2024-06"].head())
print(energy.loc["2024-06-01":"2024-06-07"])
columns = ["Consumption", "Solar", "Wind"]
energy[columns].plot(subplots=True, figsize=(12, 7))
plt.tight_layout()
plt.show()

print(energy.groupby("Month")[columns].mean())
print(energy.groupby("Weekday")["Consumption"].mean())
energy.boxplot(column="Consumption", by="Month")
plt.suptitle("")
plt.show()

sparse = energy[columns].drop(energy.index[10:13])
print(sparse.asfreq("D").iloc[8:15])
print(sparse.asfreq("D").ffill().iloc[8:15])

weekly = energy[columns].resample("W").mean()
monthly = energy[columns].resample("MS").sum(min_count=1)
annual = energy[["Consumption", "Renewables"]].resample("YS").sum(min_count=1)
annual["Renewable_share"] = annual["Renewables"] / annual["Consumption"]
print(weekly.head())
print(monthly.head())
print(annual)

smoothed = energy["Consumption"].rolling(7, center=True).mean()
trend = energy["Consumption"].rolling(365, center=True, min_periods=365).mean()
plt.figure(figsize=(12, 5))
plt.plot(energy.index, energy["Consumption"], alpha=0.3, label="Daily")
plt.plot(smoothed.index, smoothed, label="7-day average")
plt.plot(trend.index, trend, label="365-day average")
plt.ylabel("Synthetic energy units")
plt.legend()
plt.tight_layout()
plt.show()
