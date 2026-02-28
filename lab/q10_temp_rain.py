import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('q9_q10_monthly.csv')
months = df['month']
temperature = df['temperature']
rainfall = df['rainfall']

# 1. Line plot - monthly temperature
plt.figure(figsize=(10, 5))
plt.plot(months, temperature, marker='s', color='red', linewidth=2, markersize=7)
plt.title('Monthly Temperature Data - Line Plot')
plt.xlabel('Month')
plt.ylabel('Temperature (°C)')
plt.grid(True)
plt.tight_layout()
plt.savefig('q10_temperature_line.png')
plt.show()
print("Temperature line plot saved.")

# 2. Scatter plot - monthly rainfall
plt.figure(figsize=(10, 5))
plt.scatter(range(len(months)), rainfall, color='blue', s=100, zorder=5)
plt.xticks(range(len(months)), months)
plt.title('Monthly Rainfall Data - Scatter Plot')
plt.xlabel('Month')
plt.ylabel('Rainfall (mm)')
plt.grid(True)
plt.tight_layout()
plt.savefig('q10_rainfall_scatter.png')
plt.show()
print("Rainfall scatter plot saved.")
