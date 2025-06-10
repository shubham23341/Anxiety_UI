import os
from flask import Flask, request, jsonify
from flask_cors import CORS
from twilio.rest import Client

app = Flask(__name__)
CORS(app)

# Automatically fetch credentials from environment
TWILIO_ACCOUNT_SID = os.environ.get('TWILIO_ACCOUNT_SID')
TWILIO_AUTH_TOKEN = os.environ.get('TWILIO_AUTH_TOKEN')
TWILIO_PHONE_NUMBER = '+1234567890'  # Your Twilio number

@app.route('/predict', methods=['POST'])
def predict():
    data = request.get_json()
    heart_rate = data.get('heartRate')
    stress_level = data.get('stressLevel')  # Changed variable name to stress_level
    phone_number = data.get('phoneNumber')  # Provided by frontend

    # Make sure heart_rate and stress_level are numbers (int or float)
    try:
        heart_rate = float(heart_rate)
        stress_level = float(stress_level)
    except (TypeError, ValueError):
        return jsonify({"error": "Invalid input for heartRate or stressLevel"}), 400

    if heart_rate > 100 or stress_level >= 7:
        anxiety_status = "Anxiety Detected"
        if stress_level >= 9:
            anxiety_level = "High"
        elif stress_level >= 7:
            anxiety_level = "Moderate"
        else:
            anxiety_level = "Low"
    else:
        anxiety_status = "No Anxiety"
        anxiety_level = "Low"

    result = {
        "anxietyStatus": anxiety_status,
        "anxietyLevel": anxiety_level
    }

    return jsonify(result)

if __name__ == '__main__':
    app.run(debug=True)
