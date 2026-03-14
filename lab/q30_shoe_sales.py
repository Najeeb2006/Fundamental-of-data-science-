import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('shoe_sales.csv')

total = df['quantity'].sum()
df['frequency'] = df['quantity'] / total * 100

print("Shoe Size Frequency Distribution:")
print(f"{'Size':>6} | {'Quantity':>8} | {'Frequency (%)':>13}")
print("-" * 35)
for _, row in df.iterrows():
    print(f"{row['shoe_size']:>6} | {int(row['quantity']):>8} | {row['frequency']:>12.2f}%")
print("-" * 35)
print(f"{'TOTAL':>6} | {total:>8} | {'100.00%':>13}")

# Bar chart
plt.figure(figsize=(12, 5))
plt.bar(df['shoe_size'].astype(str), df['quantity'], color='skyblue', edgecolor='black')
plt.xlabel('Shoe Size')
plt.ylabel('Quantity Sold')
plt.title('Frequency Distribution of Shoe Sizes Sold')
plt.tight_layout()
plt.savefig('q30_shoe_distribution.png')
plt.show()
print("\nBar chart saved as q30_shoe_distribution.png")
