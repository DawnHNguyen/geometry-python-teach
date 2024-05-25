import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8, 8))

angle = 70

# Define the parallel lines
B = np.array([5, 1])
C = np.array([6, -1])

D = np.array([0, -1])
line_length = 4
direction = np.array([np.cos(np.radians(angle)), np.sin(np.radians(angle))])

X = D + direction * line_length

A = np.array([D[0] + direction[0]*2 + 0.05, 1])

ax.plot([A[0], B[0]], [A[1], B[1]], 'black', linewidth=2)
ax.plot([D[0], C[0]], [D[1], C[1]], 'black', linewidth=2)
ax.plot([B[0], C[0]], [B[1], C[1]], 'black', linewidth=2)

ax.plot([D[0], X[0]], [D[1], X[1]], 'black', linewidth=2)

# Annotate points
ax.text(B[0], B[1] + 0.1, 'B', fontsize=12, ha='center', color = 'b')
ax.text(C[0], C[1] - 0.2, 'C', fontsize=12, ha='center', color = 'b')
ax.text(A[0] - 0.2, A[1], 'A', fontsize=12, ha='center', color = 'b')
ax.text(D[0], D[1] - 0.2, 'D', fontsize=12, ha='center', color = 'b')
ax.text(X[0] + 0.2, X[1], 'x', fontsize=12, ha='center', color = 'b')

# Setting the plot
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_aspect('equal')

plt.box(False)
plt.show()