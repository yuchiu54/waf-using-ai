import pickle

import pandas as pd
from joblib import dump

from svm import init_svm
from rf import init_rf

def setup_pretrain_model(names, init_model_functions):
    df = pd.read_csv("../data/train_data.csv")
    for item in tuple(zip(names, init_model_functions)):
        print(item[1])
        model = item[1](df)
        dump(model, f"live/{item[0]}.joblib")

#        with open(f"../classifiers/live/{item[0]}.pkl", "wb") as file:
#            pickle.dump(model, file)
#        file.close()

#        dump(item[1], f"shadow/{item[0]}.joblib")
    print("save models to live and shadow folder")

if __name__ == "__main__":
    names = ["predictor_svm", "predictor_rf"]
    init_model_functions = [init_svm, init_rf]
    setup_pretrain_model(names, init_model_functions)
