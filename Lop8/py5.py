import matplotlib.pyplot as plt
import numpy as np

# Define the points of the quadrilateral
A = np.array([0, 4])
B = np.array([4, 4])
C = np.array([4, 0])
D = np.array([0, 0])

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the quadrilateral
ax.plot([A[0], B[0]], [A[1], B[1]], color='k')
ax.plot([B[0], C[0]], [B[1], C[1]], color='k')
ax.plot([C[0], D[0]], [C[1], D[1]], color='k')
ax.plot([D[0], A[0]], [D[1], A[1]], color='k')

# Add labels
ax.text(A[0], A[1], 'A', fontsize=12, verticalalignment='bottom')
ax.text(B[0], B[1], 'B', fontsize=12, verticalalignment='bottom')
ax.text(C[0], C[1], 'C', fontsize=12, verticalalignment='top')
ax.text(D[0], D[1], 'D', fontsize=12, verticalalignment='top')

ax.set_xticks([])
ax.set_yticks([])
ax.set_aspect('equal')

plt.box(False)
plt.show()
