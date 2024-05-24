import matplotlib.pyplot as plt
import numpy as np

# Set up the plot
fig, ax = plt.subplots()

# Define lines for xx' and yy'
ax.plot([-3, 3], [0, 0], 'k')
ax.plot([-3, 3], [-3*np.sqrt(3), 3*np.sqrt(3)], 'k')

ax.text(-3.1, 0.2, 'x\'', size=14, color='b')
ax.text(3.1, 0.2, 'x', size=14, color='b')
ax.text(-3.1, -3*np.sqrt(3) + 0.1, 'y\'', size=14, color='b')
ax.text(3.1, 3*np.sqrt(3) - 0.1, 'y', size=14, color='b')
ax.text(-0.2, 0.2, 'O', size=14, color='b')


ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])

ax.set_xlabel('')
ax.set_ylabel('')

plt.box(False)
plt.show()
