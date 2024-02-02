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

        # save the payloads and their prediction results to new_payloads.csv
        for payload, result in zip(self.payloads, self.results):
            with open("../data/new_payloads.csv", "a") as file:
                file.write(f"{payload},{result}\n")
            file.close()
        print("record sucessfully")

    def detect(self, payloads):
        self.payloads = payloads
        # predict payloads using support vector machine
        model, vectorizor, label_encoder = self.svm
        new_X = vectorizor.transform(payloads)
        predict_svm= model.predict(new_X)

        # predict payloads using random forest
        model, vectorizor, label_encoder = self.rf
        new_X = vectorizor.transform(payloads)
        predict_rf = model.predict(new_X)

        # if there's any 1 in the results, then it's considered a malformed request
        self.results = get_final_predictions(predict_svm, predict_rf)
        return any(self.results)

def get_final_predictions(lst_a, lst_b):
    if len(lst_a) != len(lst_b):
        print("The lengths of predictions from models are not equal")
        exit()
    return list(map(lambda x, y: 1 if x + y > 0 else 0, lst_a, lst_b))
