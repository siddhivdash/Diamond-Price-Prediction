import numpy as np
import pandas as pd 
from sklearn.linear_model import LinearRegression, Ridge, Lasso, ElasticNet
from src.exception import CustomException
from src.logger import logging

from src.utils import save_object
from src.utils import evaluate_model


from dataclasses import dataclass
import os
import sys

@dataclass
class ModelTrainerConfig:
    trained_model_file_path: str = os.path.join('artifacts', 'model.pkl')


class ModelTrainer:
    def __init__(self):
        self.model_trainer_config = ModelTrainerConfig()

    def initiate_model_trainer(self, train_array, test_array):
        try:
            logging.info('Splitting Dependent and Independent features from train and test data')
            X_train , y_train, X_test, y_test = (
                train_array[:,:-1], 
                train_array[:,-1], 
                test_array[:,:-1], 
                test_array[:,-1]
            )

            models ={
                'LinearRegression' : LinearRegression(),
                'Lasso' : Lasso(),
                'Ridge' : Ridge(),
                'Elastiocnet' : ElasticNet()
            }

            model_report: dict = evaluate_model(X_train, y_train, X_test, y_test, models)# evaluate_models is a utility function(in utils.py) that evaluates the models and returns a report
            print(model_report)
            print('\n===========================================================================')
            logging.info(f'Model Report: {model_report}')


            #T0 get best model score from dictionary
            best_model_score = max(sorted(model_report.values()))

            best_model_name = list(model_report.keys())[
                list(model_report.values()).index(best_model_score)
            ]

            best_model = models[best_model_name]

            print(f'Best Model Found , Model Name : {best_model_name} with score: {best_model_score}')
            print('\n===========================================================================')
            logging.info(f'Best Model Found , Model Name : {best_model_name} with score: {best_model_score}')

            save_object(
                file_path=self.model_trainer_config.trained_model_file_path, 
                obj=best_model
            )

        except Exception as e:
            logging.info('Exception occurred in Model Trainer')
            raise CustomException(e, sys)
