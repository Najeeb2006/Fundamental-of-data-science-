import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

df = pd.read_csv('q17_q19_customers.csv')
X = df[['total_spent', 'items_purchased']].values

scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# Elbow method to find optimal k
inertia = []
for k in range(1, 8):
    km = KMeans(n_clusters=k, random_state=42, n_init=10)
    km.fit(X_scaled)
    inertia.append(km.inertia_)

# Use k=4
k = 4
kmeans = KMeans(n_clusters=k, random_state=42, n_init=10)
df['cluster'] = kmeans.fit_predict(X_scaled)

print("Customer Segments Summary:")
summary = df.groupby('cluster')[['total_spent','items_purchased']].mean()
print(summary)

fig, axes = plt.subplots(1, 2, figsize=(14, 5))

# Elbow plot
axes[0].plot(range(1, 8), inertia, 'bo-')
axes[0].set_xlabel('Number of Clusters (k)')
axes[0].set_ylabel('Inertia')
axes[0].set_title('Elbow Method')

# Scatter plot
colors = ['red','blue','green','purple']
for i in range(k):
    seg = df[df['cluster'] == i]
    axes[1].scatter(seg['total_spent'], seg['items_purchased'],
                    c=colors[i], label=f'Cluster {i}', alpha=0.6)
axes[1].set_xlabel('Total Spent ($)')
axes[1].set_ylabel('Items Purchased')
axes[1].set_title('Customer Clusters')
axes[1].legend()

plt.tight_layout()
plt.savefig('q19_clusters.png')
plt.show()
print("Plot saved as q19_clusters.png")
