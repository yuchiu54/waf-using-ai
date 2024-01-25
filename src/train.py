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
        model = load_model("live", name)
        X_new = model.vectorizer.transform(new_payload)      
        y_new = model.model.predict(X_new)    
        print("X_new:", X_new)
        print("X_new:", X_new.toarray())
        print(y_new)

        model.X_train = np.concatenate([model.X_train.toarray(), X_new.toarray()])
        model.y_train = np.concatenate([model.y_train, y_new])

        model.run()
        save_model("shadow", name, model)
