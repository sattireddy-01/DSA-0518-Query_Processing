import numpy as np
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(0)
x = np.random.rand(100)
y = np.random.rand(100)

# Create scatter plot
plt.scatter(x, y, color='blue', alpha=0.5)

# Labels and Title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot of Random Distribution')

# Show plot
plt.tight_layout()
plt.show()
