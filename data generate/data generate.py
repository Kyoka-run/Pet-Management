import pandas as pd
import numpy as np

# Number of data points to generate
num_records = 1000

# Generate simulated temperature data (Celsius)
# Normal distribution with mean=38.0 and standard deviation=0.5
temperatures = np.round(np.random.normal(loc=38.0, scale=0.5, size=num_records), 2)  # Rounded to 2 decimal places

# Generate simulated heart rate data (beats per minute)
# Normal distribution with mean=80 and standard deviation=10
heartbeats = np.round(np.random.normal(loc=80, scale=10, size=num_records), 2)  # Rounded to 2 decimal places

# Define a geographic area for latitude and longitude
# For example, a small region around Dublin, Ireland
latitude_range = (53.3200, 53.3500)
longitude_range = (-6.2600, -6.2200)

# Generate random latitude values within the specified range
latitudes = np.round(np.random.uniform(low=latitude_range[0], high=latitude_range[1], size=num_records), 5)

# Generate random longitude values within the specified range
longitudes = np.round(np.random.uniform(low=longitude_range[0], high=longitude_range[1], size=num_records), 5)

# Create a DataFrame to store the generated data
data = pd.DataFrame({
    'temperature': temperatures,
    'latitude': latitudes,
    'longitude': longitudes,
    'heartbeat': heartbeats
})

# Display the first few rows of the data
print(data.head())

# Save the generated data to a CSV file
data.to_csv('simulated_pet_data.csv')
