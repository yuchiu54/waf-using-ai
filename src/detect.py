import pickle

import pandas as pd    
from sklearn import svm    
from sklearn.feature_extraction.text import CountVectorizer    
from sklearn.preprocessing import LabelEncoder    
from sklearn.model_selection import train_test_split    

from src.svm import SVMModel
from src.rf import RFModel
from src.train import load_models
from src.train import update_models

class Detector:
    def __init__(self):
        self.model_names = ["svm.pkl", "rf.pkl"]

    def find_min_MSEs_model(self, models):
        MSEs = [model.MSE for model in models]
        print("MSEs of models: ", MSEs)
        index = MSEs.index(min(MSEs))
        return models[index]

    def detect(self, payloads):
        models = load_models(self.model_names)
        model = find_min_MSEs_model(models)
        return model.predict(payloads)


def predict(model, payloads):
    return model["model"].predict(payloads)

def find_min_MSEs_model(models, model_names):
    MSEs = [model.MSE for model in models]
    print("MSEs of models: ", MSEs)
    index = MSEs.index(min(MSEs))
    return {"name": model_names[index], "model": models[index]}

def is_malicious(new_payloads):
#    new_payloads is a list since a request could have multiple payloads

    model_names = ["svm.pkl", "rf.pkl"]
    model_names = ["svm.pkl"]
    models = load_models(model_names)
    model = find_min_MSEs_model(models, model_names)

    #predict with best model
    answer = predict(model, new_payloads)
    update_models(model_names, new_payloads)
    return answer
