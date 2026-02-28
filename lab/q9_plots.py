import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv('q9_q10_monthly.csv')
months = df['month']
sales = df['sales']

# a. Line plot
plt.figure(figsize=(10, 5))
plt.plot(months, sales, marker='o', color='blue', linewidth=2, markersize=6)
plt.title('Monthly Sales Data - Line Plot')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.grid(True)
plt.tight_layout()
plt.savefig('q9_line_plot.png')
plt.show()
print("Line plot saved as q9_line_plot.png")

# b. Bar plot
plt.figure(figsize=(10, 5))
plt.bar(months, sales, color='orange', edgecolor='black')
plt.title('Monthly Sales Data - Bar Plot')
plt.xlabel('Month')
plt.ylabel('Sales ($)')
plt.tight_layout()
plt.savefig('q9_bar_plot.png')
plt.show()
print("Bar plot saved as q9_bar_plot.png")
