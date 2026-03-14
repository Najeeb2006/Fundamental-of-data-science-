import pandas as pd
import numpy as np

df = pd.read_csv('q25_population.csv')

# Mean estimation
print("=== Mean Estimation ===")
for col in ['age', 'income', 'height_cm']:
    print(f"  {col}: {df[col].mean():.2f}")

# Variance estimation
print("\n=== Variance Estimation ===")
for col in ['age', 'income', 'height_cm']:
    print(f"  {col}: {df[col].var():.2f}")

# Standard deviation
print("\n=== Standard Deviation ===")
for col in ['age', 'income', 'height_cm']:
    print(f"  {col}: {df[col].std():.2f}")

# Sampling techniques
print("\n=== Simple Random Sampling (n=20) ===")
sample = df.sample(n=20, random_state=42)
print(f"  Sample mean age:    {sample['age'].mean():.2f} (population: {df['age'].mean():.2f})")
print(f"  Sample mean income: {sample['income'].mean():.2f} (population: {df['income'].mean():.2f})")

print("\n=== Systematic Sampling (every 5th row) ===")
sys_sample = df.iloc[::5]
print(f"  Sample mean age:    {sys_sample['age'].mean():.2f}")
print(f"  Sample size: {len(sys_sample)}")
