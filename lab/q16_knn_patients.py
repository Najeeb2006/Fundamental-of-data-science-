import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score, classification_report

df = pd.read_csv('q16_patients.csv')

# Fill nulls
df['cholesterol'] = df['cholesterol'].fillna(df['cholesterol'].median())

# Encode gender
le = LabelEncoder()
df['gender'] = le.fit_transform(df['gender'])

X = df[['age', 'gender', 'blood_pressure', 'cholesterol']]
y = df['outcome']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

scaler = StandardScaler()
X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

knn = KNeighborsClassifier(n_neighbors=5)
knn.fit(X_train, y_train)
y_pred = knn.predict(X_test)

print("KNN Classification Results:")
print(f"Accuracy:  {accuracy_score(y_test, y_pred):.4f}")
print(f"Precision: {precision_score(y_test, y_pred, pos_label='Good'):.4f}")
print(f"Recall:    {recall_score(y_test, y_pred, pos_label='Good'):.4f}")
print(f"F1-Score:  {f1_score(y_test, y_pred, pos_label='Good'):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

print("Predictions on test set:")
results = pd.DataFrame({'Actual': y_test.values, 'Predicted': y_pred})
print(results.to_string(index=False))
