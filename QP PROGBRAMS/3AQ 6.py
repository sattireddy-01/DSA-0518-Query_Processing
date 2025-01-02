import numpy as np
import matplotlib.pyplot as plt

# Sample data for three groups
group1_weights = [60, 65, 70, 68, 72]
group1_heights = [160, 165, 170, 168, 175]

group2_weights = [75, 80, 85, 78, 82]
group2_heights = [170, 175, 180, 172, 178]

group3_weights = [50, 55, 60, 58, 62]
group3_heights = [150, 155, 160, 158, 165]

# Create scatter plots for each group
plt.scatter(group1_weights, group1_heights, color='red', label='Group 1', alpha=0.7)
plt.scatter(group2_weights, group2_heights, color='blue', label='Group 2', alpha=0.7)
plt.scatter(group3_weights, group3_heights, color='green', label='Group 3', alpha=0.7)

# Labels and Title
plt.xlabel('Weights (kg)')
plt.ylabel('Heights (cm)')
plt.title('Scatter Plot Comparing Weights and Heights of Three Groups')
plt.legend()

# Show plot
plt.tight_layout()
plt.show()
