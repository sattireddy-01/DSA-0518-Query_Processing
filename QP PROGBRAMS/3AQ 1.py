import numpy as np
import matplotlib.pyplot as plt

# Sample Data
categories = ['A', 'B', 'C', 'D', 'E']
means_men = [22, 30, 35, 35, 26]
means_women = [25, 32, 30, 35, 29]
std_men = [4, 3, 4, 1, 5]
std_women = [3, 5, 2, 3, 3]

# Positions for the bars
x = np.arange(len(categories))

# Bar width
bar_width = 0.6

# Plot Men
plt.bar(x, means_men, bar_width, yerr=std_men, label='Men', color='skyblue', capsize=5)

# Plot Women on top of Men
plt.bar(x, means_women, bar_width, bottom=means_men, yerr=std_women, label='Women', color='lightpink', capsize=5)

# Labels and Title
plt.xlabel('Categories')
plt.ylabel('Scores')
plt.title('Stacked Bar Plot with Error Bars')
plt.xticks(x, categories)
plt.legend()

# Show plot
plt.tight_layout()
plt.show()
