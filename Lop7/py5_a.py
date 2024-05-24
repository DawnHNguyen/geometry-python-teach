import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8, 8))

# Define origin and calculate points for lines
M = np.array([0, 0])
A = np.array([-5, 0])
B = np.array([5, 0])
D = np.array([np.cos(np.radians(180 - 45)), np.sin(np.radians(180 - 45))]) * 5

# Plot lines
ax.plot([M[0], A[0]], [M[1], A[1]], 'black', linewidth=2)
ax.plot([M[0], B[0]], [M[1], B[1]], 'black', linewidth=2)
ax.plot([M[0], D[0]], [M[1], D[1]], 'black', linewidth=2)

ax.text(A[0], A[1] + 0.2, 'A', fontsize=12, ha='center', color = 'b')
ax.text(B[0], B[1] + 0.2, 'B', fontsize=12, ha='center', color = 'b')
ax.text(D[0], D[1] + 0.2, 'D', fontsize=12, ha='center', color = 'b')
ax.text(M[0], M[1] - 0.5, 'M', fontsize=12, ha='center', color = 'b')

# Setting the plot
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel('')
ax.set_ylabel('')

plt.box(False)
plt.show()