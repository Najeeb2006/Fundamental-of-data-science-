import pandas as pd
import numpy as np
from scipy import stats

df = pd.read_csv('q27_revenue.csv')
revenue = df['revenue'].values

n = len(revenue)
mean = np.mean(revenue)
se = stats.sem(revenue)  # standard error

confidence_level = 0.95
ci = stats.t.interval(confidence_level, df=n-1, loc=mean, scale=se)

print(f"Sample size:           {n}")
print(f"Sample mean:           ${mean:.2f}")
print(f"Standard error:        ${se:.2f}")
print(f"Confidence level:      {int(confidence_level*100)}%")
print(f"Confidence Interval:   (${ci[0]:.2f}, ${ci[1]:.2f})")
print(f"\nWe are {int(confidence_level*100)}% confident that the true average revenue")
print(f"falls between ${ci[0]:.2f} and ${ci[1]:.2f}")
