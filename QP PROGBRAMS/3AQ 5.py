import numpy as np
import matplotlib.pyplot as plt

# Sample data
math_marks = [88, 92, 80, 89, 100, 80, 60, 100, 80, 34]
science_marks = [35, 79, 79, 48, 100, 88, 32, 45, 20, 30]
marks_range = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# Create scatter plot comparing Mathematics and Science marks
plt.scatter(math_marks, science_marks, color='green', alpha=0.7)

# Labels and Title
plt.xlabel('Mathematics Marks')
plt.ylabel('Science Marks')
plt.title('Scatter Plot of Mathematics vs Science Marks')
plt.xticks(marks_range)
plt.yticks(marks_range)

# Show plot
plt.tight_layout()
plt.show()
