import os
import pickle
import numpy as np
import tensorflow as tf
from sklearn.preprocessing import StandardScaler, LabelEncoder, OneHotEncoder
import pandas as pd
from app.schemas.request_model import PredictionRequest


# Get absolute path of the file
BASE_DIR = os.path.dirname(os.path.abspath(__file__))

## Load Pre-Trained Model & Preprocessing Objects 
model = tf.keras.models.load_model('app/models/model.h5')

with open(os.path.join(BASE_DIR, '../utils/label_encoder_gender.pkl'), 'rb') as file:
    label_encoder_gender = pickle.load(file)

with open(os.path.join(BASE_DIR, '../utils/on_hot_encoder_geography.pkl'), 'rb') as file:
    on_hot_encoder_geography = pickle.load(file)

with open(os.path.join(BASE_DIR, '../utils/scalar.pkl'), 'rb') as file:
    scaler = pickle.load(file)    


def churn_predict(data: PredictionRequest):
    
    # Convert categorical inputs
    print("Encoder feature names:", on_hot_encoder_geography.get_feature_names_out())

    gender = label_encoder_gender.transform([data.Gender])[0]
    geo_input_df = pd.DataFrame([[data.Geography]], columns=['Geography'])
    geography_encoded = on_hot_encoder_geography.transform(geo_input_df)
    geo_encoded_df = pd.DataFrame(geography_encoded, columns=on_hot_encoder_geography.get_feature_names_out())
    
    input_data = pd.DataFrame({
        "CreditScore": [data.CreditScore],
        "Gender": [gender],
        "Age": [data.Age],
        "Tenure": [data.Tenure],
        "Balance": [data.Balance],
        "NumOfProducts": [data.NumOfProducts],
        "HasCrCard": [data.HasCrCard],
        "IsActiveMember": [data.IsActiveMember],
        "EstimatedSalary": [data.EstimatedSalary]
    })
    
    input_data = pd.concat([input_data, geo_encoded_df], axis=1)
    input_scaled = scaler.transform(input_data)
    print(input_data.columns)
    prediction = model.predict(input_scaled)[0][0]
    
    return round(float(prediction), 2)