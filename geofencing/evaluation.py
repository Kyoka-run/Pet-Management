import pandas as pd
import time
from shapely.geometry import Point, Polygon

# Define the coordinates for the geofence
geofence_coords = [(-6.2600, 53.3500), (-6.2600, 53.3200), (-6.2200, 53.3200), (-6.2200, 53.3500)]
geofence_polygon = Polygon(geofence_coords)

# Load the simulated data
data = pd.read_csv('..\data generate\simulated_dog_health_data_complex.csv')

# Function to check if the pet is within the geofence
def check_geofence(row, polygon):
    point = Point(row['longitude'], row['latitude'])
    return polygon.contains(point)

# Apply the geofence check and record results
data['in_geofence'] = data.apply(check_geofence, polygon=geofence_polygon, axis=1)

# Calculate accuracy
accuracy = data['in_geofence'].mean()

# Simulate real-time monitoring and calculate response time
start_time = time.time()
alerts = []
for index, row in data.iterrows():
    pet_location = Point(row['longitude'], row['latitude'])
    if not geofence_polygon.contains(pet_location):
        end_time = time.time()
        response_time = end_time - start_time
        alerts.append(response_time)
        print(f"Alert! Pet {row['pet_id']} is outside the geofence. Response time: {response_time:.2f} seconds")
    else:
        print(f"Pet {row['pet_id']} is inside the geofence.")

# Calculate average response time
if alerts:
    avg_response_time = sum(alerts) / len(alerts)
else:
    avg_response_time = None

# Calculate false positive rate
# Assuming the first 100 records are used to evaluate false positives, where all should be within the geofence
false_positives = data.head(100)['in_geofence'].value_counts().get(False, 0)
false_positive_rate = false_positives / 100

# Save results to a file
with open('geofencing_test_results.txt', 'w') as file:
    file.write(f"Geofencing Accuracy: {accuracy:.4f}\n")
    if avg_response_time:
        file.write(f"Average Response Time: {avg_response_time:.2f} seconds\n")
    else:
        file.write("No boundary breaches detected, so no response time recorded.\n")
    file.write(f"False Positive Rate: {false_positive_rate:.4f}\n")
