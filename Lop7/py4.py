import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8, 8))

# Define the angle and bisector
angle = 70  # degrees
bisector_angle = angle / 2

# Define origin and calculate points for lines
O = np.array([0, 0])
M = np.array([np.cos(np.radians(0)), np.sin(np.radians(0))]) * 5  # Line Om
N = np.array([np.cos(np.radians(angle)), np.sin(np.radians(angle))]) * 5  # Line On
T = np.array([np.cos(np.radians(bisector_angle)), np.sin(np.radians(bisector_angle))]) * 5  # Line Ot (bisector)

# Plot lines
ax.plot([O[0], M[0]], [O[1], M[1]], 'black', linewidth=2)
ax.plot([O[0], N[0]], [O[1], N[1]], 'black', linewidth=2)
ax.plot([O[0], T[0]], [O[1], T[1]], 'black', linewidth=2)

ax.text(M[0], M[1] + 0.2, 'm', fontsize=12, ha='center', color = 'b')
ax.text(N[0], N[1] + 0.2, 'n', fontsize=12, ha='center', color = 'b')
ax.text(T[0], T[1] + 0.2, 't', fontsize=12, ha='center', color = 'b')
ax.text(O[0] - 0.2, O[1], 'O', fontsize=12, ha='center', color = 'b')

# Setting the plot
ax.set_xlim(-1, 6)
ax.set_ylim(-1, 6)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_aspect('equal')

plt.box(False)
plt.show()