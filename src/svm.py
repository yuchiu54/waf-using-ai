from datetime import datetime
import pickle

import pandas as pd
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from src.model_template import ModelTemplate

class SVMModel(ModelTemplate):
    def __init__(self, data):
        super()
        self.data = data
        self.vectorizer = None
        self.label_encoder = None
        self.path = "models/svm/"

    def preprocessing(self):
        vectorizer = CountVectorizer()
        X = vectorizer.fit_transform(self.data["payload"].values.astype("U"))
        self.vectorizer = vectorizer

        label_encoder = LabelEncoder()
        y = label_encoder.fit_transform(self.data["is_malicious"])
        self.label_encoder = label_encoder

        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.X_train, self.X_test, self.y_train, self.y_test = X_train, X_test, y_train, y_test

    def train(self):
        model = svm.SVC(kernel='linear', C=1.0)
        model.fit(self.X_train, self.y_train)
        self.model = model

    def predict(self, new_payload):              
        self.X_new = self.vectorizer.transform(new_payload)       
        self.y_new = self.model.predict(self.X_new)         
        values = self.label_encoder.inverse_transform(self.y_new)     
        return True if sum(values) > 0 else False
