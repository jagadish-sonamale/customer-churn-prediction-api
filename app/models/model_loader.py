# app/models/model_loader.py

import tflite_runtime.interpreter as tflite
import joblib
import os

def load_interpreter(model_path="models/model.tflite"):
    interpreter = tflite.Interpreter(model_path=model_path)
    interpreter.allocate_tensors()
    return interpreter

def load_scaler(path="models/scalar.pkl"):
    return joblib.load(path)

def load_label_encoder_gender(path="models/label_encoder_gender.pkl"):
    return joblib.load(path)

def load_one_hot_encoder_geo(path="models/on_hot_encoder_geography.pkl"):
    return joblib.load(path)
