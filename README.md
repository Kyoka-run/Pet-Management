# Pet Management System

This project is an IoT-based pet management system designed to enhance real-time health monitoring and safety for pets. The system integrates advanced machine learning algorithms, geofencing technology, and data visualization tools to provide comprehensive and actionable insights for pet owners.

## Project Structure

- **data analysis**: Contains scripts and tools used for analyzing collected data from pets, including health metrics and movement data.

- **data generate**: Scripts to generate synthetic data for testing and validation purposes, including various health conditions and geographical scenarios.

- **data wrangling**: Data preprocessing scripts for cleaning, normalizing, and transforming raw data into a format suitable for machine learning models.

- **database**: Database schema and scripts for storing and managing collected data, supporting both current and historical data analysis.

- **geofencing**: Contains the implementation of geofencing technology used to establish virtual boundaries and monitor pet movement in real-time.

- **machine learning**: Machine learning models and algorithms for detecting health anomalies in pets, including Isolation Forest, Random Forest, and K-Nearest Neighbors (KNN).

- **model evaluation**: Scripts and tools for evaluating the performance of the machine learning models, including accuracy, precision, recall, and F1 score calculations.

- **models**: Pre-trained models and configurations used in the anomaly detection and health monitoring of pets.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/pet-management-system.git
   ```

2. Navigate to the project directory:
   ```bash
   cd pet-management-system
   ```

3. Install the required dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. **Data Generation**: Generate synthetic data for testing:
   ```bash
   python data_generate/generate_data.py
   ```

2. **Data Wrangling**: Preprocess the generated or collected data:
   ```bash
   python data_wrangling/preprocess_data.py
   ```

3. **Machine Learning**: Train and evaluate the machine learning models:
   ```bash
   python machine_learning/train_model.py
   python model_evaluation/evaluate_model.py
   ```

4. **Geofencing**: Set up and monitor geofencing boundaries:
   ```bash
   python geofencing/monitor_geofence.py
   ```
