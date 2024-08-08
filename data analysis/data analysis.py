import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load processed data
data = pd.read_csv('..\\data generate\\processed_train_data.csv')

# Descriptive Statistics
def descriptive_statistics(data):
    print("Descriptive Statistics:")
    print(data.describe())

# Correlation Analysis
def correlation_analysis(data):
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Correlation Matrix')
    plt.show()

# Time Series Analysis
def time_series_analysis(data):
    # Assuming 'timestamp' column exists for time-series analysis
    data['timestamp'] = pd.to_datetime(data['timestamp'])
    data.set_index('timestamp', inplace=True)
    data[['temperature', 'heartbeat']].plot(figsize=(12, 6))
    plt.title('Time Series of Temperature and Heartbeat')
    plt.show()

# Anomaly Detection Visualization
def anomaly_detection_visualization(data):
    # This function assumes that the anomaly detection has been done and results are stored in 'anomaly' column
    plt.figure(figsize=(12, 6))
    sns.scatterplot(x=data.index, y='temperature', hue='anomaly', data=data, palette={0: 'blue', 1: 'red'})
    plt.title('Temperature Anomalies')
    plt.show()

# Run Data Analysis
descriptive_statistics(data)
correlation_analysis(data)
# time_series_analysis(data)  # Uncomment if you have a timestamp column
# anomaly_detection_visualization(data)  # Uncomment if anomaly detection results are available
