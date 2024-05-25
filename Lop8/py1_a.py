import matplotlib.pyplot as plt
import numpy as np

# Define the points for the trapezoid
A = np.array([1, 3])
B = np.array([4, 3])
C = np.array([5, 0])
D = np.array([0, 0])

# Calculate the projection of A onto line CD to find H (the foot of the altitude)
CD = C - D
CA = A - C
proj_length = np.dot(CA, CD) / np.dot(CD, CD)
H = C + proj_length * CD

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the trapezoid sides
ax.plot([A[0], B[0]], [A[1], B[1]], 'b-')
ax.plot([B[0], C[0]], [B[1], C[1]], 'b-')
ax.plot([C[0], D[0]], [C[1], D[1]], 'b-')
ax.plot([D[0], A[0]], [D[1], A[1]], 'b-')

# Plot the altitude
ax.plot([A[0], H[0]], [A[1], H[1]], 'r-')

# Add labels to the vertices
ax.text(A[0], A[1], 'A', fontsize=12, verticalalignment='bottom', horizontalalignment='right')
ax.text(B[0], B[1], 'B', fontsize=12, verticalalignment='bottom', horizontalalignment='left')
ax.text(C[0], C[1], 'C', fontsize=12, verticalalignment='top', horizontalalignment='left')
ax.text(D[0], D[1], 'D', fontsize=12, verticalalignment='top', horizontalalignment='right')
ax.text(H[0], H[1], 'H', fontsize=12, verticalalignment='top', horizontalalignment='center')

# Set limits for better visibility
ax.set_xlim(-1, 6)
ax.set_ylim(-1, 4)

# Hide ticks
ax.set_xticks([])
ax.set_yticks([])


# Show plot
plt.box(False)
plt.show()
