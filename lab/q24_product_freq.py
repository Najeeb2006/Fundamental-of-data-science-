import pandas as pd

df = pd.read_csv('q24_products.csv')

# Frequency distribution - sum times_sold per product
freq = df.groupby('product')['times_sold'].sum().reset_index()
freq = freq.sort_values('times_sold', ascending=False)
freq.columns = ['Product', 'Times Sold']

print("Frequency Distribution of Products Sold:")
print(freq.to_string(index=False))

most_popular = freq.iloc[0]
print(f"\nMost Popular Product: {most_popular['Product']} (sold {most_popular['Times Sold']} times)")
