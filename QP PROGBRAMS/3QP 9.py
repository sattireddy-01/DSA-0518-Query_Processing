import matplotlib.pyplot as plt 

languages = ['Java', 'Python', 'PHP', 'JavaScript', 'C#', 'C++']
popularity = [22.2, 17.6, 8.8, 8.0, 7.7, 6.7]
colors = ['blue', 'green', 'red', 'purple', 'orange', 'cyan']

# Vertical bar chart with different colors
plt.bar(languages, popularity, color=colors)
plt.xlabel('Programming Languages')
plt.ylabel('Popularity (%)')
plt.title('Popularity of Programming Languages (Colored Bars)')
plt.grid(axis='y', linestyle='--', linewidth=0.5)


plt.show()
