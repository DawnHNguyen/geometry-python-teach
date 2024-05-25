import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8, 8))

# Define origin and calculate points for lines
B = np.array([0, 0])
Y = np.array([-5, 0])
X = np.array([5, 0])
M = np.array([np.cos(np.radians(36)), np.sin(np.radians(36))]) * 5
N = - M

# Plot lines
ax.plot([X[0], Y[0]], [X[1], Y[1]], 'black', linewidth=2)
ax.plot([N[0], M[0]], [N[1], M[1]], 'black', linewidth=2)

ax.text(Y[0], Y[1] + 0.2, 'Y', fontsize=12, ha='center', color = 'b')
ax.text(X[0], X[1] + 0.2, 'X', fontsize=12, ha='center', color = 'b')
ax.text(M[0], M[1] + 0.2, 'M', fontsize=12, ha='center', color = 'b')
ax.text(N[0], N[1] + 0.2, 'N', fontsize=12, ha='center', color = 'b')
ax.text(B[0], B[1] - 0.5, 'B', fontsize=12, ha='center', color = 'b')

# Setting the plot
ax.set_xlim(-6, 6)
ax.set_ylim(-6, 6)
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_aspect('equal')

plt.box(False)
plt.show()