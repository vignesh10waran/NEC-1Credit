from flask import Flask, request, jsonify
import numpy as np
from ml_model import load_model, train_and_save_model

app = Flask(__name__)

# Load trained model
model = load_model()

# ------------------- PERSONAL INFO ROUTES -------------------
@app.route('/')
def home():
    """Welcome message for the API"""
    return jsonify({"message": "Welcome to the ML Model and Personal API!"})

@app.route('/name', methods=['GET'])
def get_name():
    return jsonify({"name": "vigneshwaran.m"})  # Replace with your actual name

@app.route('/register_number', methods=['GET'])
def get_register_number():
    return jsonify({"register_number": "22ITl08"})  # Replace with your register number

@app.route('/department', methods=['GET'])
def get_department():
    return jsonify({"department": "Information Technology"})  # Replace with your department

# ------------------- ML MODEL ROUTES -------------------
@app.route('/predict', methods=['POST'])
def predict():
    """Predict based on input features"""
    try:
        data = request.json
        features = np.array(data["features"]).reshape(1, -1)
        prediction = model.predict(features)
        return jsonify({"prediction": int(prediction[0])})
    except Exception as e:
        return jsonify({"error": str(e)})

@app.route('/train', methods=['GET'])
def retrain():
    """Retrain the model"""
    train_and_save_model()
    global model
    model = load_model()
    return jsonify({"message": "Model retrained successfully!"})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
