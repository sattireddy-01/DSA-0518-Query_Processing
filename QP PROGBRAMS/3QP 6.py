import matplotlib.pyplot as plt

x = [1, 2, 3, 4]
y1 = [10, 20, 25, 30]
y2 = [15, 18, 22, 28]
fig, ax = plt.subplots(2, 1)
ax[0].plot(x, y1, color='red')
ax[0].set_title('First Plot')
ax[1].plot(x, y2, color='blue')
ax[1].set_title('Second Plot')
plt.tight_layout()
plt.show()
