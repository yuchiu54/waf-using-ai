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
        self.payloads = None
        self.results = None

    def record(self):
        if self.payloads == None:
            print("record function take payloads parameter as None value")

        for payload, result in zip(self.payloads, self.results):
            with open("../data/new_payloads.csv", "a") as file:
                file.write(f"{payload},{result}\n")
            file.close()
        print("record sucessfully")

    def detect(self, payloads):
        self.payloads = payloads
        # svm
        model, vectorizor, label_encoder = self.svm
        new_X = vectorizor.transform(payloads)
        predict_svm= model.predict(new_X)

        # rf
        model, vectorizor, label_encoder = self.rf
        new_X = vectorizor.transform(payloads)
        predict_rf = model.predict(new_X)
        self.results = get_results(predict_svm, predict_rf)
        return any(self.results)

def get_results(lst_a, lst_b):
    if len(lst_a) != len(lst_b):
        print("The lengths of predictions from models are not equal")
        exit()

    results = []
    for i in range(len(lst_a)):
        result = 1 if (lst_a[i] + lst_b[i]) > 0 else 0
        results.append(result)
    return results
