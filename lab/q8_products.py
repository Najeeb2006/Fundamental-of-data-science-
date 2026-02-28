import numpy as np
import pandas as pd

df = pd.read_csv('q8_products.csv')
data = df['price'].values  # numpy array of prices

avg_price = np.mean(data)
min_price = np.min(data)
max_price = np.max(data)
total_products = len(data)

print(f"Total products analyzed: {total_products}")
print(f"Average price:  ${avg_price:.2f}")
print(f"Minimum price:  ${min_price:.2f}")
print(f"Maximum price:  ${max_price:.2f}")
