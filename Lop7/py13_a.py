import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Create a figure and an axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the vertices of the triangular prism
vertices = np.array([
    [0, 0, 0],  # A 0
    [1, 0, 0],  # B 1
    [0.5, np.sqrt(3)/2, 0],  # C 2
    [0, 0, 1],  # A' 3
    [1, 0, 1],  # B' 4
    [0.5, np.sqrt(3)/2, 1]  # C' 5
])

# Define the sides (each as a list of indices into the vertices array)
faces = [
    [vertices[0], vertices[3], vertices[4], vertices[1]],  # AA'BB'
    [vertices[0], vertices[1], vertices[2]],  # ABC
    [vertices[3], vertices[4], vertices[5]],  # A'B'C'
    [vertices[1], vertices[4], vertices[5], vertices[2]],  # BB'CC'
    [vertices[2], vertices[5], vertices[3], vertices[0]]  # CC'AA'
]

# Create a 3D polygon collection
poly3d = Poly3DCollection(faces, edgecolor='k', alpha=.25)

# Add the collection to the axes
ax.add_collection3d(poly3d)

# Auto scale to the mesh size
scale = vertices.flatten()
ax.auto_scale_xyz(scale, scale, scale)

# Removing axis labels and ticks
ax.set_xticks([])
ax.set_yticks([])
ax.set_zticks([])
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_zlabel('')

# Labels and titles
vertex_labels = ['A', 'B', 'C', "A'", "B'", "C'"]
offset = 0.03
for i, txt in enumerate(vertex_labels):
    ax.text(*vertices[i] + offset, txt, size=14, zorder=1, color='k')

ax.set_title('3D Triangular Prism')

# Show the plot
plt.show()
