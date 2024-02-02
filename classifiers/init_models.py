import pickle

import pandas as pd
from joblib import dump

from svm import init_svm
from rf import init_rf

def setup_pretrain_model(names, init_model_functions):
    df = pd.read_csv("../data/train_data.csv")
    for name, func in zip(names, init_model_functions):
        model = func(df)
        dump(model, f"live/{name}.joblib")
#        dump(item[1], f"shadow/{name}.joblib")
    print("save models to live and folder")

if __name__ == "__main__":
    names = ["predictor_svm", "predictor_rf"]
    init_model_functions = [init_svm, init_rf]
    setup_pretrain_model(names, init_model_functions)
