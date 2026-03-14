import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv('q23_credit.csv')

X = df[['income', 'credit_score', 'debt_to_income', 'employment_duration']]
y = df['risk']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# CART uses Gini impurity by default
cart = DecisionTreeClassifier(criterion='gini', max_depth=5, random_state=42)
cart.fit(X_train, y_train)
y_pred = cart.predict(X_test)

print("CART Credit Risk Model Results:")
print(f"Accuracy: {accuracy_score(y_test, y_pred):.4f}")
print("\nClassification Report:")
print(classification_report(y_test, y_pred))

# Predict for new applicant
new_applicant = [[75000, 680, 0.35, 5]]
prediction = cart.predict(new_applicant)[0]
print(f"\nNew applicant credit risk prediction: {prediction.upper()}")
print("  Income: $75,000 | Credit Score: 680 | Debt-to-Income: 35% | Employment: 5 yrs")
