import os
import pandas as pd
import joblib
from sklearn.ensemble import RandomForestClassifier

# Define relative path to load data
data_path = os.path.join('..', '..', 'data generate', 'processed_train_data.csv')

# Load the processed training data
data = pd.read_csv(data_path)

# Assume you have labels indicating normal (0) and abnormal (1) data
data['label'] = (data['temperature'] > 39) | (data['heartbeat'] > 100)  # Example condition for abnormal data

# Prepare features and labels
X = data[['temperature', 'heartbeat']]
y = data['label']

# Initialize the Random Forest model
clf = RandomForestClassifier(random_state=42)

# Train the Random Forest model
clf.fit(X, y)

# Predict and evaluate
predictions = clf.predict(X)
data['predicted_label'] = predictions

# Define relative path to save the model
model_dir = os.path.join('..', 'models')

# Create the model directory if it doesn't exist
if not os.path.exists(model_dir):
    os.makedirs(model_dir)

# Save the trained model
model_path = os.path.join(model_dir, 'random_forest_model.pkl')
joblib.dump(clf, model_path)

print(f"Random Forest model saved at {model_path}")
