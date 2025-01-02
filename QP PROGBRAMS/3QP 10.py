import matplotlib.pyplot as plt  
import numpy as np
groups = ['G1', 'G2', 'G3', 'G4', 'G5']
men_means = [22, 30, 35, 35, 26]
women_means = [25, 32, 30, 35, 29]

x = np.arange(len(groups))  # Group positions
width = 0.35  # Bar width

# Bar plot
plt.bar(x - width/2, men_means, width, label='Men', color='blue')
plt.bar(x + width/2, women_means, width, label='Women', color='pink')

plt.xlabel('Groups')
plt.ylabel('Scores')
plt.title('Scores by Group and Gender')
plt.xticks(x, groups)
plt.legend()

plt.show()
