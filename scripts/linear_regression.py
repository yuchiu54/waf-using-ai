import pickle

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

df = pd.read_csv('data/train_data.csv')

le = LabelEncoder()
df['injection_type'] = le.fit_transform(df['injection_type'])

df = pd.get_dummies(df, columns=['payload'], drop_first=True)

X = df[['injection_type'] + list(df.columns[4:])]
#X = df[['injection_type'] + list(df.columns[5:-1])]
y = df['is_malicious']


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = LinearRegression()
model.fit(X_train, y_train)

y_pred = model.predict(X_test)

mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print(f'Mean Squared Error: {mse}')
print(f'R-squared: {r2}')

with open("linear_regression.pkl", "wb") as file:
    pickle.dump(model, file)
