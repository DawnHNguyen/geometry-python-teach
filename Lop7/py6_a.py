import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8, 8))

angle = 70

# Define the parallel lines
Y = np.array([-5, 1])  # Upper parallel line start
X = np.array([5, 1])   # Upper parallel line end
Y2 = np.array([-5, -1])  # Lower parallel line start
X2 = np.array([5, -1])   # Lower parallel line end

# Calculate points for the line cutting through at 70 degrees
# Assume it cuts at the middle of the plot
A = np.array([0, 1])  # Intersection with the upper line
B = np.array([0, -1]) # Intersection with the lower line
line_length = 5
direction = np.array([np.cos(np.radians(angle)), np.sin(np.radians(angle))])

# Start and end points of the cutting line
Z = B + direction * line_length
Z2 = A - direction * line_length

# Plot parallel lines
ax.plot([Y[0], X[0]], [Y[1], X[1]], 'black', linewidth=2)
ax.plot([Y2[0], X2[0]], [Y2[1], X2[1]], 'black', linewidth=2)

# Plot cutting line
ax.plot([Z2[0], Z[0]], [Z2[1], Z[1]], 'black', linewidth=2)

# Annotate points
ax.text(Y[0], Y[1] + 0.2, 'y', fontsize=12, ha='center', color = 'b')
ax.text(X[0], X[1] + 0.2, 'x', fontsize=12, ha='center', color = 'b')
ax.text(Y2[0], Y2[1] - 0.3, 'y\'', fontsize=12, ha='center', color = 'b')
ax.text(X2[0], X2[1] - 0.3, 'x\'', fontsize=12, ha='center', color = 'b')
ax.text(A[0], A[1] + 0.2, 'A', fontsize=12, ha='center', color = 'b')
ax.text(B[0], B[1] - 0.3, 'B', fontsize=12, ha='center', color = 'b')
ax.text(Z[0] + 0.2, Z[1], 'z', fontsize=12, ha='center', color = 'b')
ax.text(Z2[0] - 0.2, Z2[1], 'z\'', fontsize=12, ha='center', color = 'b')

# Setting the plot
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel('')
ax.set_ylabel('')

plt.box(False)
plt.show()
