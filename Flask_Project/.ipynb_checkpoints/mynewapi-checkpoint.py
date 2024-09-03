# IMPORTS
from flask import Flask, request, jsonify
import joblib
import pandas as pd

# CREATE A FLASK APP
app = Flask(__name__)

# CONNECT POST API CALL ---> predict() Function
@app.route('/predict', methods=['POST'])   # means post information on "http://localhost:5000/predict" 
def predict():

    # GET JSON REQUEST
    feat_data = request.json
    # CONVERT JSON REQUEST to PANDAS DF (col names)
    df = pd.DataFrame(feat_data)
    df = df.reindex(columns=col_names)
    # PREDICT
    prediction = list(model.predict(df))
    return jsonify({'prediction': str(prediction)}) # PREDICTION


# LOAD MY MODEL and LOAD COLUMN NAMES
if __name__ == '__main__':

    model = joblib.load("final_model.pkl") 
    col_names = joblib.load("column_names.pkl") 

    app.run(debug=True)