import pandas as pd
from sklearn.ensemble import RandomForestClassifier
import pickle

# Load data
data = pd.read_csv("data_stress1.csv")

# Clean column names
data.columns = data.columns.str.strip()

# Feature and target
X = data[[
    "respiration rate", 
    "body temperature", 
    "limb movement", 
    "blood oxygen", 
    "heart rate"
]]
y = data["Stress Levels"]

# Train model
model = RandomForestClassifier()
model.fit(X, y)

# Save model
with open("model.pkl", "wb") as f:
    pickle.dump(model, f)
