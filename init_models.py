import pickle

import pandas as pd

from src.rf import RFModel
from src.svm import SVMModel

def setup_pre_trained_model(models):
    for name, model_cls in models.items():
        df = pd.read_csv("data/train_data.csv")
        model_obj = model_cls(df)
        model_obj.run()
        with open(f"models/live/{name}.pkl", "wb") as model_file:
            pickle.dump(model_obj, model_file)
        model_file.close()
    print("Sucessfully setup pre-trained model")


if __name__ == "__main__":
    models = {
        "svm": SVMModel,
        "rf": RFModel
    }
    setup_pre_trained_model(models)
