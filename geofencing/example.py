import matplotlib.pyplot as plt
from matplotlib.patches import Polygon
import geopandas as gpd
from shapely.geometry import Point, Polygon as ShapelyPolygon

# Define the geofence area using GPS coordinates
geofence_coords = [(-6.2600, 53.3500), (-6.2600, 53.3200), (-6.2200, 53.3200), (-6.2200, 53.3500)]
geofence_polygon = ShapelyPolygon(geofence_coords)

# Define the pet's path
pet_path = [(-6.2550, 53.3450), (-6.2500, 53.3400), (-6.2450, 53.3350), (-6.2400, 53.3300), (-6.2300, 53.3250)]

# Create plot
fig, ax = plt.subplots(figsize=(8, 8))

# Plot geofence
geofence_patch = Polygon(geofence_coords, closed=True, edgecolor='blue', facecolor='none', lw=2, label='Geofence')
ax.add_patch(geofence_patch)

# Plot pet path
pet_points = gpd.GeoSeries([Point(x, y) for x, y in pet_path])
pet_points.plot(ax=ax, color='red', marker='o', markersize=100, label='Pet Path')

# Highlight breach point (using the last point in the GeoSeries)
breach_point = pet_points.iloc[-1]
ax.plot(breach_point.x, breach_point.y, 'ro', markersize=15, label='Boundary Breach')

# Set plot limits and labels
ax.set_xlim(-6.2700, -6.2100)
ax.set_ylim(53.3100, 53.3600)
ax.set_xlabel('Longitude')
ax.set_ylabel('Latitude')
ax.legend()
plt.title('Geofencing Module Example Visualization')
plt.show()
