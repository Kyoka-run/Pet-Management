# Temperature vs Heartbeat Relationship Visualization
plt.figure(figsize=(8, 6))
sns.scatterplot(x='temperature', y='heartbeat', hue='anomaly', data=data, palette=['blue', 'red'])
plt.title('Temperature vs Heartbeat')
plt.xlabel('Temperature (Celsius)')
plt.ylabel('Heartbeat (bpm)')
plt.show()
