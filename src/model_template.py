from datetime import datetime
import pickle

from sklearn.metrics import mean_squared_error 

class ModelTemplate():
    def __init__(self, data):
        self.data = data
        self.X_train = None
        self.X_test = None
        self.y_train = None
        self.y_test = None
        self.model = None
        self.MSE = None

    def preprocessing(self):
        pass

    def training(self):
        pass

    def matrix(self):
        y_pred = self.model.predict(self.X_test)    
        mse = mean_squared_error(self.y_test, y_pred)    
        print(f'Mean Squared Error: {mse}')    
        self.MSE = mse

    def dump(self):
        date_id = datetime.now().strftime('%Y-%m-%d-%H:%M:%S')    
        path = self.path + date_id + ".pkl"    
        with open(path, "wb") as file:    
            pickle.dump((self.model, self.MSE), file)

    def run(self):
        self.preprocessing()        
        self.train()        
        self.matrix()
