import numpy as np
import matplotlib.pyplot as plt

# Generate random data
np.random.seed(0)
x = np.random.rand(100)
y = np.random.rand(100)
sizes = np.random.rand(100) * 100  # Random sizes for the balls

# Create scatter plot with varying ball sizes
plt.scatter(x, y, s=sizes, color='blue', alpha=0.5)

# Labels and Title
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Scatter Plot with Balls of Different Sizes')

# Show plot
plt.tight_layout()
plt.show()
