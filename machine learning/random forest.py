import pandas as pd
from sklearn.ensemble import RandomForestClassifier
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

# Train Random Forest model
print("Training Random Forest model...")
rf_model = RandomForestClassifier(n_estimators=100, random_state=42)
rf_model.fit(X_train, y_train)

# Save the Random Forest model
model_path = os.path.join(model_dir, 'random_forest_model.pkl')
joblib.dump(rf_model, model_path)
print(f"Random Forest model saved to {model_path}")
