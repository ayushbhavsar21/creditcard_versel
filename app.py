from flask import Flask, render_template, request
import os
import numpy as np
import pandas as pd
from src.credit_default.pipeline.Prediction import PredictionPipeline


app = Flask(__name__)

@app.route('/',methods=['GET'])
def homePage():
    return render_template('index.html')


@app.route('/train' ,methods=['GET'])
def training():
    os.system("python main.py")
    return "Training Successfull!"

@app.route('/predict', methods=['POST','GET'])
def index():
    
    if request.method == 'POST':
        try:
            PAY_1 = int(request.form['Repayment status in September'])
            LIMIT_BAL = int(request.form['Limit Balance'])
            BILL_AMT1 = int(request.form['First Bill Amount'])
            PAY_AMT1 = int(request.form['Payment Amount In September'])
            PAY_AMT2 = int(request.form['Payment Amount In August'])
            PAY_2 = int(request.form['Repayment status in August'])
            MARRIAGE = int(request.form['Marriage status'])
            SEX = int(request.form['Gender'])
            EDUCATION = int(request.form['Highest Education'])
            
            
            data = np.array([PAY_1,LIMIT_BAL,BILL_AMT1,PAY_AMT1,PAY_AMT2,PAY_2,MARRIAGE,SEX,EDUCATION]).reshape(1, -1)
            
            data_df = pd.DataFrame(data,columns=['PAY_1','LIMIT_BAL','BILL_AMT1','PAY_AMT1','PAY_AMT2','PAY_2','MARRIAGE','SEX','EDUCATION'])
            
            obj = PredictionPipeline()
            predict = obj.predict(data_df)
            
            return render_template('results.html', prediction = str(predict))

        except ValueError as e:
            return f"Error in processing data: {e}", 400
        except Exception as e:
            return f"An error occurred: {e}", 500
        
        
        
    else:
        return render_template('index.html')   
    
    
if __name__ == "__main__":
    app.run(port = 5000, debug=True)     