import pandas as pd

df = pd.read_csv('q12_monthly_sales.csv')

# Total quantity sold per product
top5 = df.groupby('product_name')['quantity_sold'].sum().reset_index()
top5 = top5.sort_values('quantity_sold', ascending=False).head(5)
top5.columns = ['Product Name', 'Total Quantity Sold']

print("Top 5 Products by Total Quantity Sold:")
print(top5.to_string(index=False))
