import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.cluster import KMeans
import os

# Set the working directory paths
data_dir = os.path.join('..', 'data generate')
output_dir = os.path.join('..', 'data analysis')

# Load data
data_path = os.path.join(data_dir, 'simulated_dog_health_data_complex.csv')
data = pd.read_csv(data_path)


# Descriptive Statistics
def descriptive_statistics(data):
    print("Descriptive Statistics:")
    print(data.describe())


# Correlation Analysis
def correlation_analysis(data):
    plt.figure(figsize=(10, 8))
    sns.heatmap(data.corr(), annot=True, fmt=".2f", cmap='coolwarm')
    plt.title('Correlation Matrix')
    output_path = os.path.join(output_dir, 'correlation_matrix.png')
    plt.savefig(output_path)
    plt.close()


# Data Distribution Visualization
def data_distribution_visualization(data):
    for column in ['temperature', 'heartbeat', 'activity_level', 'ambient_temperature']:
        plt.figure(figsize=(8, 6))
        sns.histplot(data[column], kde=True)
        plt.title(f'Distribution of {column}')
        output_path = os.path.join(output_dir, f'distribution_{column}.png')
        plt.savefig(output_path)
        plt.close()


# Group Comparison Analysis
def group_comparison_analysis(data):
    for column in ['temperature', 'heartbeat']:
        plt.figure(figsize=(8, 6))
        sns.boxplot(x='breed', y=column, data=data)
        plt.title(f'Breed-wise Comparison of {column}')
        output_path = os.path.join(output_dir, f'breed_comparison_{column}.png')
        plt.savefig(output_path)
        plt.close()

    plt.figure(figsize=(8, 6))
    sns.boxplot(x='gender', y='temperature', data=data)
    plt.title('Gender-wise Comparison of Temperature')
    output_path = os.path.join(output_dir, 'gender_comparison_temperature.png')
    plt.savefig(output_path)
    plt.close()


# Clustering Analysis
def clustering_analysis(data):
    kmeans = KMeans(n_clusters=3, random_state=42, n_init=10)  # Explicitly set n_init to 10
    data['cluster'] = kmeans.fit_predict(data[['temperature', 'heartbeat']])

    plt.figure(figsize=(8, 6))
    sns.scatterplot(x='temperature', y='heartbeat', hue='cluster', data=data, palette='viridis')
    plt.title('Clustering Analysis (Temperature vs Heartbeat)')
    output_path = os.path.join(output_dir, 'clustering_analysis.png')
    plt.savefig(output_path)
    plt.close()


# Run Data Analysis
descriptive_statistics(data)
correlation_analysis(data)
data_distribution_visualization(data)
group_comparison_analysis(data)
clustering_analysis(data)  # Perform clustering analysis
