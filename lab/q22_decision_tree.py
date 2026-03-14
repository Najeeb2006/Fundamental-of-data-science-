import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.preprocessing import LabelEncoder
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('q22_shoppers.csv')

# Encode categorical variable
le = LabelEncoder()
df['device_type'] = le.fit_transform(df['device_type'])

X = df[['age', 'income', 'browsing_duration', 'device_type']]
y = df['purchase']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

clf = DecisionTreeClassifier(random_state=42)
clf.fit(X_train, y_train)
y_pred = clf.predict(X_test)

print("Decision Tree Results:")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Predict for new customer
# New customer: age=30, income=60000, browsing=45min, device=mobile
device_encoded = le.transform(['mobile'])[0]
new_customer = [[30, 60000, 45.0, device_encoded]]
prediction = clf.predict(new_customer)[0]
print(f"New customer prediction: {'Will Purchase' if prediction == 1 else 'Will NOT Purchase'}")
