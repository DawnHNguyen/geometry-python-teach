import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the vertices of the pyramid
vertices = np.array([
    [0, 0, 0],  # A
    [-0.5, np.sqrt(3)/2, 0],  # B
    [0.5, np.sqrt(3)/2, 0],  # C
    [0, np.sqrt(3)/3, np.sqrt(6)/3],  # S (Tip)
    [0, np.sqrt(3)/3, 0]   # H (Altitude foot from S to base)
])

# Edges of the pyramid base and sides
edges = [
    [0, 1], [1, 2], [2, 0],  # Base Edges
    [0, 3], [1, 3], [2, 3],  # Side Edges to Tip
]

# Vector from A to H (downward to the base)
AH_vector = vertices[4] - vertices[0]
# Vector for line BC
BC_vector = vertices[2] - vertices[1]

# Solve for intersection of line AH (extended from A in direction of H) with line BC
# AH: A + t * AH_vector = p
# BC: B + s * BC_vector = q
# We find t such that p = q lies on BC
A = vertices[0]
B = vertices[1]
matrix = np.array([AH_vector, -BC_vector]).T
solution, residuals, rank, s = np.linalg.lstsq(matrix, B - A, rcond=None)
t = solution[0]

# Intersection point is A + t * AH_vector
intersection_point = A + t * AH_vector

# Plotting the vertices
ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='b')

# Plotting edges as solid lines
for edge in edges:
    points = vertices[edge]
    ax.plot(points[:, 0], points[:, 1], points[:, 2], 'b')

# Plot altitude AH extended to intersection point
ax.plot([vertices[0, 0], intersection_point[0]], [vertices[0, 1], intersection_point[1]], [vertices[0, 2], intersection_point[2]], 'b--')

# Plot altitude SH
ax.plot(vertices[[3, 4], 0], vertices[[3, 4], 1], vertices[[3, 4], 2], 'b--')

# Annotate the vertices
labels = ['A', 'B', 'C', 'S', 'H']
offset = 0.03
for i, txt in enumerate(labels):
    ax.text(vertices[i][0] + offset, vertices[i][1] + offset, vertices[i][2] + offset, txt, size=20, color='k')

# Remove the grid and axis ticks
ax.grid(False)
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])

# Optionally remove the axis labels if desired
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_zlabel('')

# Setting the axes to be equal for a more symmetric view
ax.set_box_aspect([1, 1, 1])  # Equal aspect ratio

plt.show()
