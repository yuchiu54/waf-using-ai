from datetime import datetime
import pickle

import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer    
from sklearn.preprocessing import LabelEncoder  

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

from src.model_template import ModelTemplate
#from model_template import ModelTemplate

class RFModel(ModelTemplate):
    def __init__(self, data):
        super()
        self.path = "models/rf/"
        self.data = data

#    def preprocessing(self):
#        X = self.data[['index', 'payload', 'injection_type']]
#        y = self.data['is_malicious']
#        
#        X = X.drop('index', axis=1)
#        X = pd.get_dummies(X, columns=['payload', 'injection_type'], drop_first=True)
#        
#        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
#        self.X_train, self.X_test, self.y_train, self.y_test = X_train, X_test, y_train, y_test

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
        rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
        rf_classifier.fit(self.X_train, self.y_train)
        self.model = rf_classifier

    def dump(self):
        date_id = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')         
        path = self.path + date_id + ".pkl"         
        with open(path, "wb") as file:         
            pickle.dump((self.model, self.vectorizer, self.label_encoder, self.MSE), file)

if __name__ == "__main__":    
    df = pd.read_csv("data/train_data.csv")    
    template = RFModel(df)    
    template.run()
    template.dump()
