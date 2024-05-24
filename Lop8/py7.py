import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
import numpy as np

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the square base of the pyramid centered at origin
side_length = 1  # Side length of the square base
half_side = side_length / 2
vertices = np.array([
    [-half_side, -half_side, 0],  # Vertex A
    [half_side, -half_side, 0],   # Vertex B
    [half_side, half_side, 0],    # Vertex C
    [-half_side, half_side, 0],   # Vertex D
])

# Calculate the center of the base (which will be the projection H)
H = np.mean(vertices, axis=0)

# Define the height of the pyramid
height = 1.5
# Set the apex S directly above the center H
S = np.array([H[0], H[1], H[2] + height])

# Append S and H to the vertices array
vertices = np.append(vertices, [S, H], axis=0)

# Edges connecting the base and sides
edges = [
    [0, 1], [1, 2], [2, 3], [3, 0],  # Base Edges
    [0, 4], [1, 4], [2, 4], [3, 4]   # Side Edges to Tip (S)
]

# Diagonals of the base
diagonals = [
    [0, 2],  # A to C
    [1, 3]   # B to D
]

# Plotting the vertices
ax.scatter(vertices[:, 0], vertices[:, 1], vertices[:, 2], color='b')

# Plotting edges as solid lines
for edge in edges:
    points = vertices[edge]
    ax.plot(points[:, 0], points[:, 1], points[:, 2], 'b')

# Plot the altitude from S to H
ax.plot([S[0], H[0]], [S[1], H[1]], [S[2], H[2]], 'b--')

# Plot the diagonals of the base
for diagonal in diagonals:
    points = vertices[diagonal]
    ax.plot(points[:, 0], points[:, 1], points[:, 2], 'b--')

# Annotate the verticessss
labels = ['A', 'B', 'C', 'D', 'S', 'H']
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
