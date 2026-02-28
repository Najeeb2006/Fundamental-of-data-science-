import pandas as pd

sales_data = pd.read_csv('q3_sales.csv')

# Calculate Total Sales and add as new column
sales_data['Total Sales'] = sales_data['Price'] * sales_data['Quantity']

print("Sales Data with Total Sales:")
print(sales_data.head(20).to_string(index=False))

# Summary per product
summary = sales_data.groupby('Product')['Total Sales'].sum().reset_index()
print("\nTotal Sales per Product:")
print(summary.to_string(index=False))
