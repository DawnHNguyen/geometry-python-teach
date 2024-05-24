import matplotlib.pyplot as plt
import numpy as np

fig, axs = plt.subplots(1, 3, figsize=(18, 6))

# Define points of the triangle
O = np.array([0, 0])
X = np.array([1, 3])
Y = np.array([4, 0])
Y_Folded = np.array([np.sqrt(0.4), 3*np.sqrt(0.4)])

# Triangle points and labels
triangle_points = [O, X, Y]
labels = ['O', 'x', 'y']

# Step 1: Draw the original triangle
triangle1 = plt.Polygon(triangle_points, closed=True, edgecolor='orange', facecolor='yellow', linewidth=2)
axs[0].add_patch(triangle1)
axs[0].set_title('Step 1: Original Triangle')
axs[0].set_xlim(-1, 5)
axs[0].set_ylim(-1, 4)
axs[0].set_aspect('equal', adjustable='box')
for point, label in zip(triangle_points, labels):
    axs[0].text(point[0], point[1], label, fontsize=12, ha='center')

# Step 2: Draw the folded triangle
M = (X + Y) / 2
triangle2_back = plt.Polygon([O, Y_Folded, M], closed=True, edgecolor='orange', facecolor='lightblue', linewidth=2)
triangle2_front = plt.Polygon([Y_Folded, X, M], closed=True, edgecolor='orange', facecolor='yellow', linewidth=2)
axs[1].add_patch(triangle2_front)
axs[1].add_patch(triangle2_back)
axs[1].set_title('Step 2: Folded Triangle')
axs[1].set_xlim(-1, 5)
axs[1].set_ylim(-1, 4)
axs[1].set_aspect('equal', adjustable='box')
for point, label in zip([O, X, M, Y_Folded], ['O', 'x', '', 'y']):
    axs[1].text(point[0], point[1], label, fontsize=12, ha='center')

# Step 3: Draw the triangle with bisector
triangle3 = plt.Polygon(triangle_points, closed=True, edgecolor='orange', facecolor='yellow', linewidth=2)
axs[2].add_patch(triangle3)
axs[2].plot([O[0], M[0]], [O[1], M[1]], 'red', linewidth=2)
axs[2].set_title('Step 3: Triangle with Bisector')
axs[2].set_xlim(-1, 5)
axs[2].set_ylim(-1, 4)
axs[2].set_aspect('equal', adjustable='box')
for point, label in zip(triangle_points, labels):
    axs[2].text(point[0], point[1], label, fontsize=12, ha='center')

# General settings
for ax in axs:
    ax.set_xlabel('')
    ax.set_ylabel('')
    ax.set_xticks([])
    ax.set_yticks([])

plt.show()
