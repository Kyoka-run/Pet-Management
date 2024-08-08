import pandas as pd
from sklearn.metrics import accuracy_score, precision_score, recall_score, f1_score
import joblib
import os

# Define relative paths
data_dir = os.path.join('..', 'data generate')
model_dir = os.path.join('..', 'models')
output_dir = os.path.join('..', 'model evaluation')

# Load test data
test_data = pd.read_csv(os.path.join(data_dir, 'processed_test_data.csv'))

# Separate features and labels
X_test = test_data.drop(columns=['label'])
y_test = test_data['label']

# Function to evaluate model using various metrics
def evaluate_model(model, X_test, y_test, model_name):
    y_pred = model.predict(X_test)

    # Adjust Isolation Forest predictions to match y_test labels format
    if model_name == 'isolation_forest_model.pkl':
        y_pred = [1 if pred == -1 else 0 for pred in y_pred]

    accuracy = accuracy_score(y_test, y_pred)
    precision = precision_score(y_test, y_pred)
    recall = recall_score(y_test, y_pred)
    f1 = f1_score(y_test, y_pred)

    return accuracy, precision, recall, f1

# Evaluate each model and store results
model_names = ['isolation_forest_model.pkl', 'random_forest_model.pkl', 'knn_model.pkl']
results = {}

for model_name in model_names:
    # Load the model
    model_path = os.path.join(model_dir, model_name)
    model = joblib.load(model_path)

    # Evaluate the model
    accuracy, precision, recall, f1 = evaluate_model(model, X_test, y_test, model_name)
    results[model_name] = {
        'Accuracy': accuracy,
        'Precision': precision,
        'Recall': recall,
        'F1 Score': f1
    }

# Print and save evaluation results
output_file = os.path.join(output_dir, 'model_evaluation_results.txt')

with open(output_file, 'w') as f:
    for model_name, metrics in results.items():
        result_str = (
            f"Model: {model_name}\n"
            f"Accuracy: {metrics['Accuracy']:.4f}\n"
            f"Precision: {metrics['Precision']:.4f}\n"
            f"Recall: {metrics['Recall']:.4f}\n"
            f"F1 Score: {metrics['F1 Score']:.4f}\n"
            "--------------------------------------------------\n"
        )
        print(result_str)
        f.write(result_str)

print(f"Evaluation results saved to {output_file}")

