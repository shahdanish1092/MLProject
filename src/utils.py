import pickle

from sklearn.metrics import r2_score
from sklearn.model_selection import GridSearchCV


import os
import sys

from src.Exception import CustomException


''' Save the learnt preprocessor data to the pickle file '''
def save_obj(file_path, obj):

    try:

        dir_path = os.path.dirname(file_path)

        os.makedirs(dir_path, exist_ok=True)

        with open(file_path, "wb") as file_obj:

            pickle.dump(obj,file_obj)

    except Exception as e:

        raise CustomException(e, sys)


# backward-compatible alias expected by other modules
def save_object(file_path, obj):
    return save_obj(file_path, obj)


def load_model(file_path: str):

    try:
        with open(file_path, 'rb') as file_obj:
            return pickle.load(file_obj)

    except Exception as e:
        raise CustomException(e, sys)




def evaluate_models(X_train, y_train, X_test, y_test, params, models):

    try:

        report = {}

        for i in range(len(list(models))):

            model = list(models.values())[i]

            para = params[list(models.keys())[i]]


            gs = GridSearchCV(model, para, cv=3)

            gs.fit(X_train, y_train)


            model.set_params(**gs.best_params_)

            model.fit(X_train, y_train)

            y_train_pred = model.predict(X_train)

            y_test_pred = model.predict(X_test)

            train_score = r2_score(y_train, y_train_pred)

            test_score = r2_score(y_test, y_test_pred)

            report[list(models.keys())[i]] = test_score

        return report




    except Exception as e:

        raise CustomException(e, sys)

             




def load_model(file_path):

    try:

        with open(file_path, "rb") as file_obj:

            return pickle.load(file_obj)

    except Exception as e:

        raise CustomException(e, sys)

