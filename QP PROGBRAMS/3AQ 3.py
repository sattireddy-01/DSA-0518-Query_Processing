import numpy as np
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(0)
x = np.random.rand(100)
y = np.random.rand(100)

# Create scatter plot with empty circles
plt.scatter(x, y, edgecolor='red', facecolor='none', alpha=0.7)

# Labels and Title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Empty Circles')

# Show plot
plt.tight_layout()
plt.show()
