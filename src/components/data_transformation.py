from sklearn.compose import ColumnTransformer
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import OneHotEncoder, StandardScaler

from sklearn.pipeline import Pipeline


from dataclasses import dataclass

import os
import sys
import numpy as np
import pandas as pd

from src.Exception import CustomException
from src.Logger import logging
from src.utils import save_obj





@dataclass
class DataTransformationConfig:

    preprocessor_obj_file_path = os.path.join('artifacts', "preprocessor.pkl")


class DataTransformation:

    def __init__(self):

        self.preprocessor_config = DataTransformationConfig()


    def get_data_transformed(self):

        try:

            num_col = ["writing_score", "reading_score"]

            cat_col = [
                "gender",
                "race_ethnicity",
                "parental_level_of_education",
                "lunch",
                "test_preparation_course",
            ]



            num_pipeline = Pipeline(
                steps=[
                    ("imputing", SimpleImputer(strategy="median")),
                    ("scaling",StandardScaler())
                ]
            )

            cat_pipeline = Pipeline(
                steps=[
                    ("imputer", SimpleImputer(strategy="most_frequent")),
                    ("onehotencoding", OneHotEncoder()),
                    ("scaler", StandardScaler(with_mean=False))
                ]
            )



            logging.info(f"Numerical Columns: {num_col}")
            logging.info(f"Categorical Columns: {cat_col}")

            preprocessor = ColumnTransformer(
                transformers=[
                    ("num_pipeline", num_pipeline, num_col),
                    ("cat_pipeline", cat_pipeline, cat_col),
                ],
                remainder='drop',
            )




            return preprocessor





        except Exception as e:

            raise CustomException(e,sys)





    def initiate_data_transformation(self, train_path, test_path):

        try:

            train_df = pd.read_csv(train_path)
            test_df = pd.read_csv(test_path)

            logging.info("Data segregation of the train and testing")
            logging.info("Getting the preprocessor oj from the preprocessor function")

            target_col = "math_score"


            preprocessor_obj = self.get_data_transformed()


            input_feature_train_df = train_df.drop(columns=[target_col])
            target_train_df = train_df[target_col]


            input_feature_test_df = test_df.drop(columns=[target_col])
            target_test_df = test_df[target_col]

            logging.info("Applying preprocessing on the trainand test df ......")


            transformed_train_df = preprocessor_obj.fit_transform(input_feature_train_df)
            transformed_test_df = preprocessor_obj.transform(input_feature_test_df)


            train_arr = np.c_[transformed_train_df, np.array(target_train_df)]
            test_arr = np.c_[transformed_test_df, np.array(target_test_df)]


            logging.info("Saved preprocessing object.")

            save_obj(

                file_path = self.preprocessor_config.preprocessor_obj_file_path,
                obj = preprocessor_obj
                 
            )



            return (
                train_arr,
                test_arr,
                self.preprocessor_config.preprocessor_obj_file_path,
            )





        except Exception as e:
            raise CustomException(e, sys)
