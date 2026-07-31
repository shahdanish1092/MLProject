import os
import sys
from pathlib import Path
from dataclasses import dataclass

PROJECT_ROOT = Path(__file__).resolve().parents[2]
if str(PROJECT_ROOT) not in sys.path:
    sys.path.append(str(PROJECT_ROOT))

import pandas as pd
from sklearn.model_selection import train_test_split

from src.components.data_transformation import DataTransformation
from src.components.data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainer
from src.components.model_trainer import ModelTrainerConfig

from src.Exception import CustomException
from src.Logger import logging


@dataclass
class DataIngestionConfig():

    train_path: str = str(PROJECT_ROOT / "artifacts" / "train.csv")
    test_path: str = str(PROJECT_ROOT / "artifacts" / "test.csv")
    raw_data_path: str = str(PROJECT_ROOT / "artifacts" / "data.csv")


class DataIngestion():

    def __init__(self):

        self.ingestion_config = DataIngestionConfig()

    def ingestion_pipeline(self):

        logging.info("Entered the data ingestion pipeline......")

        try:

            data_path = PROJECT_ROOT / 'notebook' / 'data' / 'stud.csv'
            df = pd.read_csv(data_path)

            logging.info("Read the datset as dataframe")

            os.makedirs(PROJECT_ROOT / 'artifacts', exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)

            logging.info("Splitting the data")

            train_set, test_set = train_test_split(df, test_size=0.2, random_state=42)

            train_set.to_csv(self.ingestion_config.train_path, index=False, header=True)

            test_set.to_csv(self.ingestion_config.test_path, index=False, header=True)


            return (
                self.ingestion_config.train_path,
                self.ingestion_config.test_path
            )

        except Exception as e:

            raise CustomException(e, sys)


if __name__ == "__main__":

    obj = DataIngestion()
    train_data, test_data = obj.ingestion_pipeline()


    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)


    modeltrainer=ModelTrainer()
    print(modeltrainer.initiate_model_training(train_arr,test_arr))