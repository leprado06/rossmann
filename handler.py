import pickle
import os
import json
import pandas as pd
from flask              import Flask, request, Response
from rossmann.Rossmann  import Rossmann

#loading model
model = pickle.load(open('model/model_rossmann.pkl','rb'))

#initialize api
app = Flask(__name__)

@app.route('/rossmann/predict',methods=['POST'])
def rossmann_predict():
    test_json = request.get_json()
    if test_json:
        if isinstance(test_json, dict):
            test_raw = pd.DataFrame(test_json, index=[0])
        else:
            test_raw = pd.DataFrame(test_json, columns=test_json[0].keys())

        pipeline = Rossmann()

        #data cleaning
        df1 = pipeline.data_cleaning(test_raw)
        #feature Engineering
        df2 = pipeline.feature_engineering(df1)
        #data preparation
        df3 = pipeline.data_preparation(df2)
        #predict
        df_response = pipeline.get_prediction( model, test_raw, df3)

        return df_response
    else:
        return Response ('{}',status = 200, mimetype='application/json')

if __name__ == '__main__':
    port = os.environ.get('PORT', 5000)
    app.run(host = '0.0.0.0', port = port)