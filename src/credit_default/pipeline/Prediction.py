import joblib 
import numpy as np
import pandas as pd
from pathlib import Path



class PredictionPipeline:
    def __init__(self):
        self.model = joblib.load(Path('artifacts/model_trainer/model.joblib'))

    
    def predict(self, data):
        prediction = self.model.predict(data)

        if(prediction == 0):
          return "Not going to Default on payment"
        else:
            return "Most Likely to Default on Payment"