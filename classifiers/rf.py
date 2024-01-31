from datetime import datetime
import pickle

import pandas as pd

from sklearn.feature_extraction.text import CountVectorizer    
from sklearn.preprocessing import LabelEncoder  

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def init_rf(df):
    vectorizer = CountVectorizer()    
    X = vectorizer.fit_transform(df["payload"].values.astype("U"))

    label_encoder = LabelEncoder()    
    y = label_encoder.fit_transform(df["is_malicious"])

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)    

    rf_classifier = RandomForestClassifier(n_estimators=100, random_state=42)
    rf_classifier.fit(X_train, y_train)
    return rf_classifier, vectorizer, label_encoder
