import pickle

import joblib
import pandas as pd    
from joblib import dump, load
from sklearn import svm    
from sklearn.feature_extraction.text import CountVectorizer    
from sklearn.preprocessing import LabelEncoder    
from sklearn.model_selection import train_test_split    

class Detector:
    def __init__(self):
        self.svm = load("../classifiers/live/predictor_svm.joblib")
        self.rf = load("../classifiers/live/predictor_rf.joblib")

    def load_model(self, file_path):
        with open(file_path, "rb") as file:
            model = pickle.load(file)
        file.close()
        return model

    def detect(self, payloads):
        # svm
        model, vectorizor, label_encoder = self.svm
        new_X = vectorizor.transform(payloads)
        predict_svm= model.predict(new_X)
#        model.fit(new_X, predict_svm)
#        dump("../classifiers/shadow/svm.joblib")

        # rf
        model, vectorizor, label_encoder = self.rf
        new_X = vectorizor.transform(payloads)
        predict_rf = model.predict(new_X)
#        model.fit(new_X, predict_rf)
#        dump("../classifiers/shadow/rf.joblib")

        value = sum(predict_svm) + sum(predict_rf)
        return True if value > 0 else False
