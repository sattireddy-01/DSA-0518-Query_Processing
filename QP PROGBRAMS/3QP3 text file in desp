import matplotlib.pyplot as plt

# Reading data from the file
x, y = [], []
with open('C:/Users/bhadr/OneDrive/Desktop/test.txt', 'r') as file:  # Correct path
    for line in file:
        values = line.split()
        x.append(int(values[0]))
        y.append(int(values[1]))

# Plotting the data
plt.plot(x, y, label="Line from file data", color="blue")
plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Line Plot from File Data')
plt.legend()
plt.show()
