import matplotlib.pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d.art3d import Poly3DCollection

# Create a figure and an axes
fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')

# Define the vertices of the quadrilateral vertical prism
# Base vertices are A, B, C, D and their corresponding top vertices are A', B', C', D'
vertices = np.array([
    [0.5, 0, 0],  # A 0
    [2, -0.5, 0],  # B 1
    [3, 4, 0],  # C 2
    [0, 4, 0],  # D 3
    [0.5, 0, 4],  # A' 4
    [2, -0.5, 4],  # B' 5
    [3, 4, 4],  # C' 6
    [0, 4, 4]   # D' 7
])

# Define the sides (each as a list of indices into the vertices array)
faces = [
    [vertices[0], vertices[1], vertices[2], vertices[3]],  # ABCD
    [vertices[4], vertices[5], vertices[6], vertices[7]],  # A'B'C'D'
    [vertices[0], vertices[4], vertices[5], vertices[1]],  # AA'BB'
    [vertices[1], vertices[5], vertices[6], vertices[2]],  # BB'CC'
    [vertices[2], vertices[6], vertices[7], vertices[3]],  # CC'DD'
    [vertices[3], vertices[7], vertices[4], vertices[0]]   # DD'AA'
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
vertex_labels = ['A', 'B', 'C', 'D', "A'", "B'", "C'", "D'"]
offset = 0.05  # Adjust offset if necessary for visibility
for i, txt in enumerate(vertex_labels):
    ax.text(*(vertices[i] + offset), txt, size=14, zorder=1, color='k')

ax.set_title('3D Quadrilateral Vertical Prism')

# Show the plot
plt.show()
