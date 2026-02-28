import pandas as pd

property_data = pd.read_csv('q4_property.csv')

# 1. Average listing price per location
avg_price = property_data.groupby('location')['listing_price'].mean().reset_index()
avg_price.columns = ['location', 'avg_listing_price']
print("1. Average listing price per location:")
print(avg_price.to_string(index=False))

# 2. Number of properties with more than 4 bedrooms
count_4plus = property_data[property_data['bedrooms'] > 4].shape[0]
print(f"\n2. Properties with more than 4 bedrooms: {count_4plus}")

# 3. Property with the largest area
largest = property_data.loc[property_data['area_sqft'].idxmax()]
print(f"\n3. Property with largest area:")
print(largest.to_string())
