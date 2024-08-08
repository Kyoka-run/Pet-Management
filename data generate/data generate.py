import pandas as pd
import numpy as np

# Number of data points to generate
num_records = 2000

# Generate pet ID
pet_ids = np.arange(1, num_records + 1)

# Generate gender (0: Female, 1: Male)
genders = np.random.choice([0, 1], size=num_records)

# Generate breed types (0: Small, 1: Medium, 2: Large, 3: Giant)
# Assume different breeds might have different normal ranges for heart rate and temperature
breeds = np.random.choice([0, 1, 2, 3], size=num_records)

# Generate age (in years)
# Assuming a typical dog age distribution
ages = np.round(np.random.uniform(0.5, 15.0, size=num_records), 1)

# Generate simulated body temperature data (Celsius)
# Breed-based normal temperature ranges
normal_temp_ranges = {
    0: (38.5, 39.0),  # Small breed
    1: (38.3, 38.8),  # Medium breed
    2: (38.0, 38.5),  # Large breed
    3: (37.8, 38.3)   # Giant breed
}

temperatures = np.array([
    np.round(np.random.normal(
        loc=np.mean(normal_temp_ranges[breed]),
        scale=0.3 if breed != 3 else 0.4), 2)
    for breed in breeds
])

# Introduce temperature anomalies
fever_temperatures = np.round(np.random.uniform(low=39.5, high=41.0, size=int(0.1 * num_records)), 2)
hypothermia_temperatures = np.round(np.random.uniform(low=36.0, high=37.0, size=int(0.05 * num_records)), 2)
anomalous_temperatures = np.concatenate([fever_temperatures, hypothermia_temperatures])
temperatures[:len(anomalous_temperatures)] = anomalous_temperatures
np.random.shuffle(temperatures)

# Generate simulated heart rate data (beats per minute)
# Breed-based normal heart rate ranges
normal_hr_ranges = {
    0: (90, 140),   # Small breed
    1: (80, 120),   # Medium breed
    2: (60, 100),   # Large breed
    3: (50, 90)     # Giant breed
}

heartbeats = np.array([
    np.round(np.random.uniform(low=normal_hr_ranges[breed][0], high=normal_hr_ranges[breed][1]), 2)
    for breed in breeds
])

# Introduce heart rate anomalies
high_heartbeats = np.round(np.random.uniform(low=140, high=200, size=int(0.1 * num_records)), 2)
low_heartbeats = np.round(np.random.uniform(low=30, high=60, size=int(0.05 * num_records)), 2)
anomalous_heartbeats = np.concatenate([high_heartbeats, low_heartbeats])
heartbeats[:len(anomalous_heartbeats)] = anomalous_heartbeats
np.random.shuffle(heartbeats)

# Add noise to heart rate data to simulate sensor inaccuracies
noise = np.random.normal(0, 1.0, num_records)
heartbeats = np.round(heartbeats + noise, 2)

# Define a geographic area for latitude and longitude around a typical dog park
latitude_range = (53.3200, 53.3500)  # Example area: Dublin, Ireland
longitude_range = (-6.2600, -6.2200)
latitudes = np.round(np.random.uniform(low=latitude_range[0], high=latitude_range[1], size=num_records), 5)
longitudes = np.round(np.random.uniform(low=longitude_range[0], high=longitude_range[1], size=num_records), 5)

# Generate activity levels for dogs (0: resting, 1: light, 2: moderate, 3: intense)
activity_levels = np.random.choice([0, 1, 2, 3], size=num_records, p=[0.4, 0.3, 0.2, 0.1])

# Generate ambient temperature data (Celsius) relevant to outdoor conditions
normal_ambient_temp = np.round(np.random.normal(loc=18.0, scale=5.0, size=int(0.8 * num_records)), 2)
extreme_ambient_temp = np.round(np.random.uniform(low=5.0, high=35.0, size=int(0.2 * num_records)), 2)
ambient_temperatures = np.concatenate([normal_ambient_temp, extreme_ambient_temp])
np.random.shuffle(ambient_temperatures)

# Create a DataFrame to store the generated data
data = pd.DataFrame({
    'pet_id': pet_ids,
    'gender': genders,
    'breed': breeds,
    'age': ages,
    'temperature': temperatures,
    'latitude': latitudes,
    'longitude': longitudes,
    'heartbeat': heartbeats,
    'activity_level': activity_levels,
    'ambient_temperature': ambient_temperatures
})

# Display the first few rows of the data
print(data.head())

# Save the generated data to a CSV file
data.to_csv('simulated_dog_health_data_complex.csv', index=False)

