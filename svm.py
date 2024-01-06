import pandas as pd
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split
import pickle

data = pd.read_csv("payloads.csv")
#data = pd.read_csv("payload_full.csv")

vectorizer = CountVectorizer()
print(type(data["payload"][0]))
X = vectorizer.fit_transform(data["payload"].values.astype("U"))

label_encoder = LabelEncoder()
y = label_encoder.fit_transform(data["is_malicious"])

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

svm_model = svm.SVC(kernel='linear', C=1.0)
svm_model.fit(X_train, y_train)

accuracy = svm_model.score(X_test, y_test)
print("Accuracy:", accuracy)

with open('svm_model_for_anomaly_detection.pkl', 'wb') as model_file:
    pickle.dump((svm_model, vectorizer, label_encoder), model_file)
