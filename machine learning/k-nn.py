import pandas as pd
from sklearn.neighbors import KNeighborsClassifier
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

# Train K-Nearest Neighbors model with optimized parameters
print("Training K-Nearest Neighbors model...")
knn_model = KNeighborsClassifier(n_neighbors=6, weights='distance', metric='minkowski')  # Optimized parameters
knn_model.fit(X_train, y_train)

# Save the K-Nearest Neighbors model
model_path = os.path.join(model_dir, 'knn_model.pkl')
joblib.dump(knn_model, model_path)
print(f"K-Nearest Neighbors model saved to {model_path}")

