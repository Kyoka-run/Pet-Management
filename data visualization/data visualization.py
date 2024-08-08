# Heartbeat Distribution Visualization
plt.figure(figsize=(10, 4))
sns.histplot(data['heartbeat'], kde=True, color='green')
plt.title('Heartbeat Distribution')
plt.xlabel('Heartbeat (bpm)')
plt.ylabel('Frequency')
plt.show()
