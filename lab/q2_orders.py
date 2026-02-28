import pandas as pd

df = pd.read_csv('q2_orders.csv')
df['order_date'] = pd.to_datetime(df['order_date'])

# 1. Total orders per customer
orders_per_customer = df.groupby('customer_id').size().reset_index(name='total_orders')
print("1. Total orders per customer:")
print(orders_per_customer.to_string(index=False))

# 2. Average order quantity per product
avg_qty = df.groupby('product_name')['order_quantity'].mean().reset_index()
avg_qty.columns = ['product_name', 'avg_quantity']
print("\n2. Average order quantity per product:")
print(avg_qty.to_string(index=False))

# 3. Earliest and latest order dates
print(f"\n3. Earliest order date: {df['order_date'].min().date()}")
print(f"   Latest order date:   {df['order_date'].max().date()}")
