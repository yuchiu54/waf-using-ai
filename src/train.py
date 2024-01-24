import pickle

import numpy as np
from scipy.sparse import hstack, vstack

from src.svm import SVMModel
from src.rf import RFModel

def load_model(mode:str, model_name):
    with open(f"models/{mode}/{model_name}", "rb") as model_file:
        model = pickle.load(model_file)
    return model

def load_models(model_names):
    models = []
    for name in model_names:    
        with open(f"models/live/{name}", "rb") as model_file:    
            models.append(pickle.load(model_file))    
        model_file.close()    
    return models

def save_model(mode: str, model_type: str, model):
    # param:mode -> live or shadow
    if mode == "live":
        with open(f"models/live/{model_type}", "wb") as model_file:
            pickle.dump(model, model_file)
        model_file.close()

    if mode == "shadow":
        with open(f"models/shadow/{model_type}", "wb") as model_file:
            pickle.dump(model, model_file)
        model_file.close()

def update_models(model_names, new_payload):    
    for name in model_names:
        # load existing model and X and y values    
        model = load_model("live", name)
        # load new_X and new_y values, in this case it's new payloads    
        X_new = model.vectorizer.transform(new_payload)      
        y_new = model.model.predict(X_new)    
        # combine existing and new X and y values    
        model.X_train = vstack([model.X_train, X_new])
        # hstack([sparse_matrix, dense_array])
        model.y_train = vstack([model.y_train, y_new])
        # fit    
        model.model.run()
        # dump    
        save_model("shadow", name, model)
