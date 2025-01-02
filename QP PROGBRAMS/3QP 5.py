import matplotlib.pyplot as plt
x=[1,2,3,4,5]
y=[1,2,3,4,5]

x2 = [1, 2, 3, 4, 5]
y2 = [5, 4, 3, 2, 1]

plt.plot(x,y,color="red",label="X and Y Points ni Represent chestundii")
plt.plot(x2, y2, color="blue", label="Line 2: X and Reversed Y Points")

plt.xlabel('X-axis')
plt.ylabel('Y-axis')
plt.title('Drawing a line between X and Y axis')
plt.legend()
plt.show()


