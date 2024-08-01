import matplotlib.pyplot as plt
import seaborn as sns

# Temperature Distribution Visualization
plt.figure(figsize=(10, 4))
sns.histplot(data['temperature'], kde=True, color='blue')
plt.title('Temperature Distribution')
plt.xlabel('Temperature (Celsius)')
plt.ylabel('Frequency')
plt.show()
