import sys
import pandas as pd
from src.Exception import CustomException
from src.utils import load_model


import os






class Predictdata:

    def __init__(self):
        pass


    def predict_point(self, features):

        try:  
            model_path = os.path.join('artifacts', "model.pkl")
            model = load_model(file_path=model_path)

            preprocessr_path = os.path.join('artifacts', "preprocessor.pkl")
            preprocessr = load_model(file_path=preprocessr_path)


            data_scaled = preprocessr.transform(features)
            preds = model.predict(data_scaled)

            return preds

        except Exception as e:

            raise CustomException(e, sys)


    def predict(self, features):
        """Compatibility wrapper used by the web app."""
        return self.predict_point(features)






class CustomData:

    try:


        def __init__(self,
            gender: str,
            race_ethnicity: str,
            parental_level_of_education,
            lunch: str,
            test_preparation_course: str,
            reading_score: int,
            writing_score: int):


            self.gender = gender

            self.race_ethnicity = race_ethnicity

            self.parental_level_of_education = parental_level_of_education

            self.lunch = lunch

            self.test_preparation_course = test_preparation_course

            self.reading_score = reading_score

            self.writing_score = writing_score



        def get_data_from_dataframe(self):

            customdata_input_featuures = {

                "gender": [self.gender],
                "race_ethnicity": [self.race_ethnicity],
                "parental_level_of_education": [self.parental_level_of_education],
                "lunch": [self.lunch],
                "test_preparation_course": [self.test_preparation_course],
                "reading_score": [self.reading_score],
                "writing_score": [self.writing_score],

            }


            return pd.DataFrame(customdata_input_featuures)


    except Exception as e:
        raise CustomException(e, sys)