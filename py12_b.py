import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the vertices of the cube
vertices = np.array([
    [0, 0, 0],  # B
    [1, 0, 0],  # C
    [1, 1, 0],  # D
    [0, 1, 0],  # A
    [0, 0, 1],  # N
    [1, 0, 1],  # M
    [1, 1, 1],  # P
    [0, 1, 1]   # Q
])

# Create a list of edges connecting the vertices
edges = [
    [0, 1], [1, 2], [2, 3], [3, 0],  # Bottom Face
    [4, 5], [5, 6], [6, 7], [7, 4],  # Top Face
    [0, 4], [1, 5], [2, 6], [3, 7]   # Side Edges
]

# Distinguish front and back edges
front_edges = [[0, 1], [1, 2], [5, 6], [6, 7], [1, 5], [2, 6], [4, 7], [4, 5], [0, 4]]
back_edges = [[3, 7], [3, 0], [2, 3]]

# Plot the vertices
ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='b')

# Plot front edges as solid lines
for edge in front_edges:
    points = vertices[edge]
    ax.plot(points[:, 0], points[:, 1], points[:, 2], 'b')

# Plot back edges as dashed lines
for edge in back_edges:
    points = vertices[edge]
    ax.plot(points[:, 0], points[:, 1], points[:, 2], 'b--')  # Dashed line

# Annotate the vertices
labels = ['B', 'C', 'D', 'A', 'B\'', 'C\'', 'D\'', 'A\'']
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
ax.set_box_aspect([3, 2, 1])  # Equal aspect ratio

plt.show()
