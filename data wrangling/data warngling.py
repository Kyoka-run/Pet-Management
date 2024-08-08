import pandas as pd
from sklearn.model_selection import train_test_split

# Load the generated complex data
data = pd.read_csv('..\data generate\simulated_dog_health_data_complex.csv')

# Select relevant features for machine learning
features = data[['gender', 'breed', 'age', 'temperature', 'heartbeat', 'activity_level', 'ambient_temperature']]
labels = data.apply(lambda row: 1 if row['temperature'] > 39.5 or row['temperature'] < 37.0 or row['heartbeat'] > 140 or row['heartbeat'] < 60 else 0, axis=1)

# Split the data into training and testing sets (70% train, 30% test)
X_train, X_test, y_train, y_test = train_test_split(features, labels, test_size=0.3, random_state=42)

# Combine features and labels, and name the label column explicitly
train_data = pd.concat([X_train, y_train], axis=1)
train_data.columns = list(X_train.columns) + ['label']
test_data = pd.concat([X_test, y_test], axis=1)
test_data.columns = list(X_test.columns) + ['label']

# Save the processed data
train_data.to_csv('..\data generate\processed_train_data.csv', index=False)
test_data.to_csv('..\data generate\processed_test_data.csv', index=False)

print("Data processing completed. Training and testing data saved.")
