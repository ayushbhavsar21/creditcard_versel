﻿import pandas as pd
import os
from credit_default import logger
from sklearn.ensemble import RandomForestClassifier # type: ignore
import joblib
from credit_default.entity.config_entity import ModelTrainerConfig


class ModelTrainer:
    def __init__(self, config: ModelTrainerConfig):
        self.config = config


    
    def train(self):
        train_data = pd.read_csv(self.config.train_data_path)
        test_data = pd.read_csv(self.config.test_data_path)


        train_x = train_data.drop([self.config.target_column], axis=1)
        test_x = test_data.drop([self.config.target_column], axis=1)
        train_y = train_data[[self.config.target_column]].values.ravel() 
        test_y = test_data[[self.config.target_column]].values.ravel() 


        rfc = RandomForestClassifier(n_estimators=self.config.n_estimators, criterion=self.config.criterion, random_state=42)
        rfc.fit(train_x, train_y)

        joblib.dump(rfc, os.path.join(self.config.root_dir, self.config.model_name))