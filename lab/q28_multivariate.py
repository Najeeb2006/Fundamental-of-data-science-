import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import scatter_matrix

df = pd.read_csv('q28_cars.csv')

# Multivariate Scatter Plot (horsepower vs mpg colored by make)
makes = df['make'].unique()
colors = ['red', 'blue', 'green', 'orange', 'purple']
make_color = {make: colors[i] for i, make in enumerate(makes)}

plt.figure(figsize=(10, 6))
for make in makes:
    subset = df[df['make'] == make]
    plt.scatter(subset['horsepower'], subset['mpg'], label=make,
                color=make_color[make], alpha=0.7)
plt.xlabel('Horsepower')
plt.ylabel('MPG')
plt.title('Horsepower vs MPG by Car Make')
plt.legend()
plt.tight_layout()
plt.savefig('q28_multivariate_scatter.png')
plt.show()

# Scatter Plot Matrix
numeric_cols = ['horsepower', 'mpg', 'price', 'weight_lbs']
fig, ax = plt.subplots(figsize=(12, 10))
scatter_matrix(df[numeric_cols], alpha=0.5, figsize=(12, 10), diagonal='kde')
plt.suptitle('Scatter Plot Matrix - Car Dataset', y=1.02)
plt.tight_layout()
plt.savefig('q28_scatter_matrix.png')
plt.show()
print("Plots saved as q28_multivariate_scatter.png and q28_scatter_matrix.png")
