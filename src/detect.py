import pickle

import pandas as pd    
from sklearn import svm    
from sklearn.feature_extraction.text import CountVectorizer    
from sklearn.preprocessing import LabelEncoder    
from sklearn.model_selection import train_test_split    

from src.svm import SVMModel
from src.rf import RFModel

def load_models(filenames):
    models = []
    for name in filenames:
        with open("src/models/{}".format(name), "rb") as model_file:
            models.append(pickle.load(model_file))
        model_file.close()
    return models

def predict(model, payloads):
    if model["name"] == "svm.pkl":
        answer = svm_predict(model["model"], payloads)
    elif model["name"] == "rf.pkl":
        answer = rf_predict(model["model"], payloads)
    return answer
    
def svm_predict(model, new_payload):
    print("using svm")
    svm_model, vectorizer, label_encoder, MSE = model
    X_new = vectorizer.transform(new_payload)
    numerical_prediction = svm_model.predict(X_new)
    values = label_encoder.inverse_transform(numerical_prediction)
    return True if sum(values) > 0 else False

def rf_predict(model, new_payload):
    print("using rf")
    rf_model, vectorizer, label_encoder, MSE = model
    X_new = vectorizer.transform(new_payload)
    numerical_prediction = rf_model.predict(X_new)
    values = label_encoder.inverse_transform(numerical_prediction)
    return True if sum(values) > 0 else False

def find_min_MSEs_model(models, model_names):
    MSEs = [model[-1] for model in models]
    print("MSEs of models: ", MSEs)
    index = MSEs.index(min(MSEs))
    return {"name": model_names[index], "model": models[index]}

def update_models():
#    update all models -> at each model combine data and train using XXXModel
    pass

def is_malicious(new_payloads):
#    new_payloads is a list since a request could have multiple payloads

    model_names = ["svm.pkl", "rf.pkl"]
    models = load_models(model_names)
    model = find_min_MSEs_model(models, model_names)

    #predict with best model
    answer = predict(model, new_payloads)
    update_models()
    return answer
