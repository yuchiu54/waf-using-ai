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
    def __init__(self, mode):
        self.mode = mode
        self.model_names = ["svm.pkl", "rf.pkl"]

    def find_min_MSEs_model(self, models):
        MSEs = [model.MSE for model in models]
        index = MSEs.index(min(MSEs))
        return models[index]

    def detect(self, payloads):
        models = load_models(self.mode, self.model_names)
        model = self.find_min_MSEs_model(models)
        return model.predict(payloads)

    def analysis(self, payloads):
        models = load_models(self.mode, self.model_names)
        for model in models:
            model.predict(payloads)
