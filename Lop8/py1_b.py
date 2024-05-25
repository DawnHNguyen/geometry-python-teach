import matplotlib.pyplot as plt
import numpy as np

# Define the coordinates for the trapezoid vertices
A = np.array([1, 3])
B = np.array([3, 3])
C = np.array([4, 1])
D = np.array([0, 1])

# Create a figure and an axes
fig, ax = plt.subplots()

# Plot the sides of the trapezoid
ax.plot([A[0], B[0]], [A[1], B[1]], 'b-')
ax.plot([B[0], C[0]], [B[1], C[1]], 'b-')
ax.plot([C[0], D[0]], [C[1], D[1]], 'b-')
ax.plot([D[0], A[0]], [D[1], A[1]], 'b-')

# Add labels to the vertices
ax.text(A[0], A[1], 'A', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
ax.text(B[0], B[1], 'B', fontsize=12, verticalalignment='bottom', horizontalalignment='left')
ax.text(C[0], C[1], 'C', fontsize=12, verticalalignment='top', horizontalalignment='left')
ax.text(D[0], D[1], 'D', fontsize=12, verticalalignment='top', horizontalalignment='right')

# Set the plot limits for better visibility
ax.set_xlim(-1, 5)
ax.set_ylim(0, 4)

# Remove ticks from both axes
ax.set_xticks([])
ax.set_yticks([])

# Display the plot
plt.box(False)
plt.show()
