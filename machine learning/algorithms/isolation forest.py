import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

# Define relative paths
data_path = os.path.join('..','..', 'data generate', 'processed_train_data.csv')
model_dir = os.path.join('..','..', 'machine learning', 'models')

# Load the processed training data
data = pd.read_csv(data_path)

# Initialize the Isolation Forest model
model = IsolationForest(contamination=0.05, random_state=42)

# Train the model using the loaded data
features = data[['temperature', 'heartbeat']]
model.fit(features)

# Predict anomalies
predictions = model.predict(features)

# Mark anomalies in the data
data['anomaly'] = predictions
anomalies = data[data['anomaly'] == -1]

print(f"Number of anomalies detected: {len(anomalies)}")

# Create the model directory if it doesn't exist
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

# Save the trained model
model_path = os.path.join(model_dir, 'isolation_forest_model.pkl')
joblib.dump(model, model_path)



