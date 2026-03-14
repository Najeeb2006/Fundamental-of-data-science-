import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('q17_q19_customers.csv')

X = df[['total_spent', 'visit_frequency']].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# K-Means with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(X_scaled)

print("Customer Segmentation Results:")
for i in range(3):
    seg = df[df['cluster'] == i]
    print(f"\nCluster {i} ({len(seg)} customers):")
    print(f"  Avg Total Spent:     ${seg['total_spent'].mean():.2f}")
    print(f"  Avg Visit Frequency: {seg['visit_frequency'].mean():.2f}")

# Scatter plot
colors = ['red', 'blue', 'green']
plt.figure(figsize=(8, 6))
for i in range(3):
    seg = df[df['cluster'] == i]
    plt.scatter(seg['total_spent'], seg['visit_frequency'],
                c=colors[i], label=f'Cluster {i}', alpha=0.6)
plt.xlabel('Total Spent ($)')
plt.ylabel('Visit Frequency')
plt.title('Customer Segments (K-Means)')
plt.legend()
plt.tight_layout()
plt.savefig('q17_clusters.png')
plt.show()
print("\nPlot saved as q17_clusters.png")
