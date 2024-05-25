import matplotlib.pyplot as plt

# Set up the plot
fig, ax = plt.subplots()

# Define lines for xx' and yy'
ax.plot([-3, 3], [3, -3], 'k')
ax.plot([-3, 3], [-3, 3], 'k')

ax.text(-2.9, 3.1, 'x', size=14, color='b')
ax.text(3.1, -2.9, "x'", size=14, color='b')
ax.text(-2.8, -3.1, 'y', size=14, color='b')
ax.text(3.1, 2.9, "y'", size=14, color='b')
ax.text(0, 0.2, 'O', size=14, color='b')


ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])

ax.set_xlabel('')
ax.set_ylabel('')
ax.set_aspect('equal')

plt.box(False)
plt.show()
