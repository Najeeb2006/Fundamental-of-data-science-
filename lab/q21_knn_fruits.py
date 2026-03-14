import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.preprocessing import StandardScaler
from sklearn.metrics import accuracy_score

df = pd.read_csv('q21_fruits.csv')

# color and texture are already encoded as integers in CSV
X = df[['weight', 'color', 'texture']].values
y = df['type'].values

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Find optimal k
best_k, best_acc = 1, 0
for k in range(1, 11):
    knn = KNeighborsClassifier(n_neighbors=k)
    knn.fit(X_train, y_train)
    acc = accuracy_score(y_test, knn.predict(X_test))
    if acc > best_acc:
        best_acc, best_k = acc, k

print(f"Optimal k = {best_k} with accuracy = {best_acc:.4f}")

# Train with best k
knn = KNeighborsClassifier(n_neighbors=best_k)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

print("\nPredictions vs Actual:")
for actual, pred in zip(y_test[:10], y_pred[:10]):
    print(f"  Actual: {actual:8s} | Predicted: {pred}")

# Predict unknown fruit
unknown = scaler.transform([[180, 2, 1]])  # weight=180g, color=2, texture=1
print(f"\nPredicted fruit type for unknown sample: {knn.predict(unknown)[0]}")
