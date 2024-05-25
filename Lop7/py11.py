import matplotlib.pyplot as plt
import numpy as np

# Define the base points B and C
B = np.array([0, 0])
C = np.array([4, 0])

# Calculate the midpoint of BC, which will also be the foot of the altitude from A
D = (B + C) / 2

# Define point A such that AB = AC, creating an isosceles triangle
# Assuming the height of the triangle is arbitrary, let's say 3 units above D
A = np.array([D[0], 3])

# Create a figure and axis
fig, ax = plt.subplots()

# Plot the triangle sides
ax.plot([A[0], B[0]], [A[1], B[1]], 'b-', label='AB')
ax.plot([A[0], C[0]], [A[1], C[1]], 'b-', label='AC')
ax.plot([B[0], C[0]], [B[1], C[1]], 'b-', label='BC')

# Plot the altitude from A to BC
ax.plot([A[0], D[0]], [A[1], D[1]], 'r--', label='Altitude')

# Add labels to the vertices
ax.text(A[0], A[1], 'A', fontsize=12, verticalalignment='bottom', horizontalalignment='center')
ax.text(B[0], B[1], 'B', fontsize=12, verticalalignment='top', horizontalalignment='right')
ax.text(C[0], C[1], 'C', fontsize=12, verticalalignment='top', horizontalalignment='left')
ax.text(D[0], D[1], 'D', fontsize=12, verticalalignment='top', horizontalalignment='center')

# Set limits for better visibility
ax.set_xlim(-1, 5)
ax.set_ylim(-1, 4)

# Hide ticks
ax.set_xticks([])
ax.set_yticks([])

# Equal aspect ratio to ensure angles are shown correctly
ax.set_aspect('equal')

# Show plot
plt.box(False)
plt.show()
