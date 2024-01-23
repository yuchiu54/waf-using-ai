from datetime import datetime
import pickle

import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.preprocessing import LabelEncoder, OneHotEncoder
from sklearn.compose import ColumnTransformer

from src.model_template import ModelTemplate
#from model_template import ModelTemplate

class LRModel(ModelTemplate):
    def __init__(self, data):
        super()
        self.path = "models/lr/"
        self.data = data

    def preprocessing(self):
        le = LabelEncoder()
        self.data['injection_type'] = le.fit_transform(self.data['injection_type'])
        self.data = pd.get_dummies(self.data, columns=['payload'], drop_first=True)
        X = self.data[['injection_type'] + list(self.data.columns[4:])]
        y = self.data['is_malicious']

#        vectorizer = CountVectorizer()    
#        X = vectorizer.fit_transform(self.data["payload"].values.astype("U"))    
#        self.vectorizer = vectorizer    
    
        label_encoder = LabelEncoder()    
        y = label_encoder.fit_transform(self.data["is_malicious"])    
        self.label_encoder = label_encoder
        
        X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
        self.X_train, self.X_test, self.y_train, self.y_test = X_train, X_test, y_train, y_test
        
    def train(self):
        model = LinearRegression()
        model.fit(self.X_train, self.y_train)
        self.model = model

    def dump(self):                          
        date_id = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')         
        path = self.path + date_id + ".pkl"         
        with open(path, "wb") as file:         
            pickle.dump((self.model, self.vectorizer, self.label_encoder, self.MSE), file)
        
if __name__ == "__main__":
    # loading
    df = pd.read_csv("data/train_data.csv")
    template = LRModel(df)
    template.run()    
    template.dump()
