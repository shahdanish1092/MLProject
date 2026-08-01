
import os
import sys
from dataclasses import dataclass

from pathlib import Path


PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:

    sys.path.append(str(PROJECT_ROOT))

from src.components.data_ingestion import DataIngestion
from src.components.data_transformation import DataTransformation
from src.components.model_trainer import ModelTrainer
from src.Exception import CustomException

from src.Logger import logging

import pandas as pd
import numpy as np








@dataclass
class TrainingPipelineConfig:

    artifacts_dir:str = os.path.join("artifacts")



class TrainingPipeline:

    def __init__(self):

        self.training_pipeline_config = TrainingPipelineConfig()




    def run_pipeline(self):

        try:

            data_ingestion = DataIngestion()

            train_path, test_path = data_ingestion.ingestion_pipeline()

            data_transformation = DataTransformation()

            train_arr, test_arr, preprocessor_path = data_transformation.initiate_data_transformation(train_path, test_path)

            model_trainer = ModelTrainer()

            r2_score = model_trainer.initiate_model_training(train_arr, test_arr)

            return{
                "train_path": train_path,
                "test_path": test_path,
                "preprocessor_path": preprocessor_path,
                "r2_score": r2_score
            }

        except Exception as e:

            raise CustomException(e, sys)



if __name__ == "__main__":

    result = TrainingPipeline().run_pipeline()
    print(result)
            



