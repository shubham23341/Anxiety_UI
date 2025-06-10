import requests

url = 'http://127.0.0.1:5000/predict'
payload = {
    "respiration rate": 16,
    "body temperature": 98.6,
    "limb movement": 3,
    "blood oxygen ": 97,
    "heart rate ": 80,
    "Stress Level": 2
}

try:
    response = requests.post(url, json=payload)
    print("Status Code:", response.status_code)
    print("Response Text:", response.text)
except Exception as e:
    print("Error occurred:", e)
