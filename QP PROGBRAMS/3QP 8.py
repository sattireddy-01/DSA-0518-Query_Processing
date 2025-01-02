import matplotlib.pyplot as plt

# Data
languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]

# Horizontal bar chart
plt.barh(languages, popularity, color='skyblue')
plt.xlabel('Popularity (%)')
plt.ylabel('Programming Languages')
plt.title('Popularity of Programming Languages')
plt.grid(axis='x', linestyle='--', linewidth=0.5)

# Display the chart
plt.show()
