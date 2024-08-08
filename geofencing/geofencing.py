import os
import pandas as pd
from shapely.geometry import Point, Polygon

# Step 1: Define the geofence polygon
# Define a polygon representing the geofence (e.g., a square around a specific area)
# Coordinates are in the form (longitude, latitude)
geofence_coords = [(-6.2600, 53.3500), (-6.2600, 53.3200), (-6.2200, 53.3200), (-6.2200, 53.3500)]
geofence_polygon = Polygon(geofence_coords)

# Step 2: Load pet location data (latitude, longitude)
# Example DataFrame of pet locations
# In a real scenario, this could be replaced with a data loading mechanism from a file or a real-time data stream
data = pd.DataFrame({
    'latitude': [53.3310, 53.3150, 53.3400],
    'longitude': [-6.2510, -6.2750, -6.2300]
})

# Step 3: Function to check if each point is inside the geofence
def check_geofence(row, polygon):
    point = Point(row['longitude'], row['latitude'])
    return polygon.contains(point)

# Step 4: Apply the function to each row in the DataFrame
data['in_geofence'] = data.apply(check_geofence, polygon=geofence_polygon, axis=1)

# Display the results
print("Geofencing Check Results:")
print(data)

# Step 5: Simulate real-time monitoring
print("\nReal-time Monitoring Simulation:")
for index, row in data.iterrows():
    pet_location = Point(row['longitude'], row['latitude'])
    if geofence_polygon.contains(pet_location):
        print(f"At time {index}, Pet is inside the geofence.")
    else:
        print(f"At time {index}, Pet is outside the geofence!")
