import pandas as pd
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
import joblib

# Load your dataset
data = pd.read_csv("data_stress1.csv")

# Print columns to confirm actual names
print("Available columns:", data.columns)

# Define features and label — make sure these column names match your CSV exactly
X = data[['respiration rate', 'body temperature', 'limb movement', 'blood oxygen ', 'heart rate ', 'Stress Levels']]
y = data['Stress Levels']  # Adjust this if your label column is named differently

# Split the data
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

# Train the model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model
joblib.dump(model, 'model.pkl')

print("✅ Model training complete and saved as model.pkl")
