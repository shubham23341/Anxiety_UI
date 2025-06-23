import os
import joblib
from flask import Flask, request, jsonify
from flask_cors import CORS

app = Flask(__name__)
CORS(app)

# Load the trained model
model = joblib.load('model.pkl')

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    try:
        heart_rate = float(data.get('heartRate'))
        temperature = float(data.get('temperature'))
        spo2 = float(data.get('spo2'))
        limb_movement = float(data.get('limbMovement'))
        respiration_rate = float(data.get('respirationRate'))
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input"}), 400

    input_features = [[heart_rate, temperature, spo2, limb_movement, respiration_rate]]

    print("📥 Received data:", input_features)  # Debug log

    try:
        predicted_stress = model.predict(input_features)[0]
        print("📤 Predicted stress level:", predicted_stress)

        anxiety_level = (
            "High" if predicted_stress >= 9 else
            "Moderate" if predicted_stress >= 7 else
            "Low"
        )

        return jsonify({
            "predictedStressLevel": round(predicted_stress, 2),
            "anxietyLevel": anxiety_level
        })

    except Exception as e:
        return jsonify({"error": f"Prediction error: {str(e)}"}), 500

if __name__ == '__main__':
    app.run(debug=True)
