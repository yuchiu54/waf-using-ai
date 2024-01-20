
"""
Todo:
    in is_malicious() get prediction scores from all the models and choose the best one as model to detect
"""

import pandas as pd    
from sklearn import svm    
from sklearn.feature_extraction.text import CountVectorizer    
from sklearn.preprocessing import LabelEncoder    
from sklearn.model_selection import train_test_split    
import pickle

def is_malicious(new_payload):
    with open('svm.pkl', 'rb') as model_file:
        loaded_svm_model, loaded_vectorizer, loaded_label_encoder = pickle.load(model_file)
    
#    new_payload = ["www.example.com", "c/ caridad s/n"]
    X_new = loaded_vectorizer.transform(new_payload)
    
    numerical_prediction = loaded_svm_model.predict(X_new)
    
    values = loaded_label_encoder.inverse_transform(numerical_prediction)
    return True if sum(values) > 0 else False
