from datetime import datetime
import pickle

import pandas as pd
from sklearn import svm
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder
from sklearn.model_selection import train_test_split

from src.model_template import ModelTemplate
#from model_template import ModelTemplate

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

    def dump(self):                          
        date_id = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')         
        path = self.path + date_id + ".pkl"         
        with open(path, "wb") as file:         
            pickle.dump((self.model, self.vectorizer, self.label_encoder, self.MSE), file)

if __name__ == "__main__":
    df = pd.read_csv("data/train_data.csv")
    template = SVMModel(df)
    template.run()
    template.dump()
