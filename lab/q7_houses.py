import numpy as np
import pandas as pd

df = pd.read_csv('q7_houses.csv')
house_data = df.values  # Convert to numpy array

bedrooms_col = 0
price_col = 2

# Filter houses with more than 4 bedrooms
mask = house_data[:, bedrooms_col] > 4
filtered = house_data[mask]

avg_price = np.mean(filtered[:, price_col])

print(f"Total houses: {len(house_data)}")
print(f"Houses with more than 4 bedrooms: {len(filtered)}")
print(f"Average sale price (>4 bedrooms): ${avg_price:,.2f}")

print("\nSample filtered houses:")
print("Bedrooms | Sqft | Sale Price")
for row in filtered[:5]:
    print(f"  {int(row[0])}      | {int(row[1])} | ${int(row[2]):,}")
