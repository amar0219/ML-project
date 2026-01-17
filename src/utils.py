import os 
import sys
import numpy as np
import pandas as pd
import pickle
import dill
from src.exception import CustomException
from sklearn.metrics import r2_score

def save_object(file_path, obj):
    """Saves a Python object to a file using pickle."""
    try:
        dir_path=os.path.dirname(file_path)
        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, 'wb') as file_obj:
            dill.dump(obj, file_obj)
    except Exception as e:
        raise CustomException(e, sys)
    
def evaluate_models(X_train, y_train, X_test, y_test, models):
    """Evaluates multiple regression models and returns their R2 scores."""
    try:
        report = {}
        for i in range(len(models)):
            model = list(models.values())[i]
            # Train the model
            model.fit(X_train, y_train)
            y_train_pred = model.predict(X_train)

            # Calculating R2 score
            r2_square_train = r2_score(y_train, y_train_pred)

            # Predicting the test set results
            y_test_pred = model.predict(X_test)

            # Calculating R2 score
            r2_square_test = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = r2_square_test
        return report
    except Exception as e:
        raise CustomException(e, sys)