import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv('customer_reviews.csv')

category = 'Electronics'
cat_df = df[df['category'] == category]['rating']

n = len(cat_df)
mean_rating = cat_df.mean()
se = stats.sem(cat_df)
ci = stats.t.interval(0.95, df=n-1, loc=mean_rating, scale=se)

print(f"Category: {category}")
print(f"Number of reviews: {n}")
print(f"Average rating: {mean_rating:.2f} / 5.0")
print(f"95% Confidence Interval: ({ci[0]:.2f}, {ci[1]:.2f})")

# Satisfaction level
if mean_rating >= 4.0:
    satisfaction = "High"
elif mean_rating >= 3.0:
    satisfaction = "Medium"
else:
    satisfaction = "Low"
print(f"Customer satisfaction level: {satisfaction}")

# All categories summary
print("\nAll Categories Summary:")
summary = df.groupby('category')['rating'].agg(['count', 'mean', 'std'])
print(summary.round(2))
