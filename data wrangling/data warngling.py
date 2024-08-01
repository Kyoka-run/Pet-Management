import pandas as pd
from sklearn.preprocessing import StandardScaler
from sklearn.model_selection import train_test_split
import os

# Define the relative path to the data file
data_path = os.path.join('..', 'data generate', 'simulated_pet_data.csv')

# Load the dataset using the relative path
data = pd.read_csv(data_path)

# Feature selection (only using temperature and heartbeat)
features = data[['temperature', 'heartbeat']]

# Data normalization
scaler = StandardScaler()
features_scaled = scaler.fit_transform(features)

# Split data into training (70%) and testing (30%) sets
X_train, X_test = train_test_split(features_scaled, test_size=0.3, random_state=42)

# 将处理后的数据保存为新的CSV文件
processed_data = pd.DataFrame(features_scaled, columns=['temperature', 'heartbeat'])

# 将训练集和测试集保存到不同的文件
train_data = pd.DataFrame(X_train, columns=['temperature', 'heartbeat'])
test_data = pd.DataFrame(X_test, columns=['temperature', 'heartbeat'])

# Define paths for saving the processed data
train_data_path = os.path.join('..', 'data generate', 'processed_train_data.csv')
test_data_path = os.path.join('..', 'data generate', 'processed_test_data.csv')

# Save the processed training and testing data
train_data.to_csv(train_data_path, index=False)
test_data.to_csv(test_data_path, index=False)

