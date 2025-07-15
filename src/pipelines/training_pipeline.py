import sys
import os

# Add the root directory to sys.path
ROOT_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
sys.path.insert(0, ROOT_DIR)

from src.logger import logging
from src.exception import CustomException

import pandas as pd

from src.components.data_transformation import DataTransformation
from src.components.data_ingestion import DataIngestion

from src.components.model_trainer import ModelTrainer


from src.components.data_ingestion import DataIngestion

if __name__ == "__main__":
    obj = DataIngestion()
    train_data_path, test_data_path = obj.initiate_data_ingestion()
    print(train_data_path, test_data_path)

    data_traformation = DataTransformation()

    train_arr,test_arr,_ = data_traformation.initiate_data_transformation(train_data_path, test_data_path)


    model_trainer = ModelTrainer()
    model_trainer.initiate_model_trainer(train_arr, test_arr)




