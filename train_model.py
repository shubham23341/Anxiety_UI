import pandas as pd
from sklearn.ensemble import RandomForestRegressor
import joblib

# Load data
data = pd.read_csv("data_stress1.csv")
data.columns = data.columns.str.strip()  # Remove accidental spaces

# Print to confirm
print("✅ Available columns:", data.columns.tolist())

# Use the corrected column names
X = data[['heart rate', 'body temperature', 'blood oxygen', 'limb movement', 'respiration rate']]
y = data['Stress Levels']

# Train model
model = RandomForestRegressor()
model.fit(X, y)

# Save model
joblib.dump(model, 'model.pkl')
print("✅ Model trained and saved as model.pkl")
