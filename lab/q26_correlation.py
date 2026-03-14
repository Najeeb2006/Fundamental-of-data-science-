import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

df = pd.read_csv('q26_weather.csv')

temp = df['temperature']
rain = df['rainfall_mm']

# Pearson correlation
corr = np.corrcoef(temp, rain)[0, 1]
print(f"Correlation coefficient (r) between temperature and rainfall: {corr:.4f}")

if abs(corr) < 0.3:
    strength = "weak"
elif abs(corr) < 0.7:
    strength = "moderate"
else:
    strength = "strong"
direction = "positive" if corr > 0 else "negative"
print(f"Interpretation: {strength} {direction} correlation")

# Scatter plot
plt.figure(figsize=(8, 6))
plt.scatter(temp, rain, alpha=0.6, color='blue', edgecolors='black')
m, b = np.polyfit(temp, rain, 1)
x_line = np.linspace(temp.min(), temp.max(), 100)
plt.plot(x_line, m * x_line + b, color='red', label=f'y = {m:.2f}x + {b:.2f}')
plt.xlabel('Temperature (°C)')
plt.ylabel('Rainfall (mm)')
plt.title(f'Temperature vs Rainfall (r = {corr:.4f})')
plt.legend()
plt.tight_layout()
plt.savefig('q26_correlation.png')
plt.show()
print("Scatter plot saved as q26_correlation.png")
