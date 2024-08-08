import pandas as pd
from sklearn.ensemble import IsolationForest
import joblib
import os

# Define relative paths
data_dir = os.path.join('..', 'data generate')
model_dir = os.path.join('..', 'models')

# Load processed training and testing data
train_data = pd.read_csv(os.path.join(data_dir, 'processed_train_data.csv'))
test_data = pd.read_csv(os.path.join(data_dir, 'processed_test_data.csv'))

# Separate features and labels
X_train = train_data.drop(columns=['label'])
y_train = train_data['label']
X_test = test_data.drop(columns=['label'])
y_test = test_data['label']

# Train Isolation Forest model with optimized parameters
print("Training Isolation Forest model...")
iso_forest = IsolationForest(n_estimators=300, contamination=0.15, max_samples=0.9, random_state=42)
iso_forest.fit(X_train)

# Save the Isolation Forest model
model_path = os.path.join(model_dir, 'isolation_forest_model.pkl')
joblib.dump(iso_forest, model_path)
print(f"Isolation Forest model saved to {model_path}")
