# app/models/predict.py

import numpy as np
import pandas as pd

from app.models.model_loader import (
    load_interpreter,
    load_scaler,
    load_label_encoder_gender,
    load_one_hot_encoder_geo
)

# Load model + encoders once
interpreter = load_interpreter()
label_encoder_gender = load_label_encoder_gender()
on_hot_encoder_geography = load_one_hot_encoder_geo()
scaler = load_scaler() 


def preprocess_input(data):
    gender = label_encoder_gender.transform([data.Gender])[0]
    geo_df = pd.DataFrame([[data.Geography]], columns=['Geography'])
    geo_encoded = on_hot_encoder_geography.transform(geo_df)
    geo_encoded_df = pd.DataFrame(geo_encoded, columns=on_hot_encoder_geography.get_feature_names_out())

    input_data = pd.DataFrame({
        "CreditScore": [data.CreditScore],
        "Gender": [gender],
        "Age": [data.Age],
        "Tenure": [data.Tenure],
        "Balance": [data.Balance],
        "NumOfProducts": [data.NumOfProducts],
        "HasCrCard": [data.HasCrCard],
        "IsActiveMember": [data.IsActiveMember],
        "EstimatedSalary": [data.EstimatedSalary],
    })

    input_data = pd.concat([input_data, geo_encoded_df], axis=1)
    input_scaled = scaler.transform(input_data).astype(np.float32)

    return input_scaled

def run_inference(input_scaled):
    input_details = interpreter.get_input_details()
    output_details = interpreter.get_output_details()

    interpreter.set_tensor(input_details[0]['index'], input_scaled)
    interpreter.invoke()

    prediction = interpreter.get_tensor(output_details[0]['index'])[0][0]
    return round(float(prediction), 2)
