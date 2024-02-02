import pickle

import pandas as pd
from joblib import dump

from svm import train_svm
from rf import train_rf

def train_models(df, mode, names, init_model_functions):
    for name, func in zip(names, init_model_functions):
        # init model with init_functions
        model = func(df)
        # save the model to a file named "name" in live folder
        dump(model, f"{mode}/{name}.joblib")
    print(f"save models to {mode} and folder")
    
def combine_df(df_paths):    
    if len(df_paths) < 1 or df_paths == None:
        print("df_paths is requried")

    # load new input payload data    
    df = pd.read_csv("../data/train_data.csv")    
    df = df[["payload", "is_malicious"]]    

    for new_path in df_paths:
        new_df = pd.read_csv(new_path)    
        df = pd.concat([df, new_df])    
    df = df.drop_duplicates(subset=["payload"])
    return df

if __name__ == "__main__":
    # Todo:
    #       implement a command line interface to allow users to choose 
    #       between initializing a model or retraining an existing one.
    names = ["predictor_svm", "predictor_rf"]
    init_model_functions = [train_svm, train_rf]
    df = pd.read_csv("../data/train_data.csv")
#    train_models(df, "live", names, init_model_functions)
    df = combine_df(["../data/new_payloads.csv"])
#    train_models(df, "shadow", names, init_model_functions)
