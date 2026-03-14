import pandas as pd
import numpy as np

df = pd.read_csv('q18_temperatures.csv')

# 1. Mean temperature per city
mean_temp = df.groupby('city')['temperature'].mean()
print("1. Mean Temperature per City:")
for city, val in mean_temp.items():
    print(f"   {city}: {val:.2f}°C")

# 2. Standard deviation per city
std_temp = df.groupby('city')['temperature'].std()
print("\n2. Standard Deviation per City:")
for city, val in std_temp.items():
    print(f"   {city}: {val:.2f}°C")

# 3. City with highest temperature range
city_stats = df.groupby('city')['temperature'].agg(['max', 'min'])
city_stats['range'] = city_stats['max'] - city_stats['min']
highest_range_city = city_stats['range'].idxmax()
print(f"\n3. City with highest temperature range: {highest_range_city} "
      f"({city_stats.loc[highest_range_city,'range']:.2f}°C)")

# 4. City with most consistent temperature (lowest std)
most_consistent = std_temp.idxmin()
print(f"\n4. City with most consistent temperature: {most_consistent} "
      f"(std = {std_temp[most_consistent]:.2f}°C)")
