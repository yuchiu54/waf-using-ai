import pickle

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

df = pd.read_csv("data/train_data.csv")

X = df[['index', 'payload', 'injection_type']]
y = df['is_malicious']

X = X.drop('index', axis=1)

X = pd.get_dummies(X, columns=['payload', 'injection_type'], drop_first=True)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
rf_classifier.fit(X_train, y_train)



y_pred = rf_classifier.predict(X_test)

accuracy = accuracy_score(y_test, y_pred)
print(f"Accuracy: {accuracy:.2f}")

print("Classification Report:")
print(classification_report(y_test, y_pred))

with open('random_forest.pkl', 'wb') as model_file:    
    pickle.dump(rf_classifier, model_file)
