import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots(figsize=(8, 8))

X = np.array([-2, 1])
Y = np.array([3, 1])
X2 = np.array([-2, -1])
Y2 = np.array([3, -1])
H = np.array([0, 1])
K = np.array([0, -1])
Z = np.array([0, 2])
Z2 = np.array([0, -2])

# Plot parallel lines
ax.plot([Y[0], X[0]], [Y[1], X[1]], 'black', linewidth=2)
ax.plot([Y2[0], X2[0]], [Y2[1], X2[1]], 'black', linewidth=2)
ax.plot([Z[0], Z2[0]], [Z[1], Z2[1]], 'black', linewidth=2)

# Annotate points
ax.text(Y[0], Y[1] + 0.1, 'y', fontsize=12, ha='center', color = 'b')
ax.text(X[0], X[1] + 0.1, 'x', fontsize=12, ha='center', color = 'b')
ax.text(Y2[0], Y2[1] - 0.2, 'y\'', fontsize=12, ha='center', color = 'b')
ax.text(X2[0], X2[1] - 0.2, 'x\'', fontsize=12, ha='center', color = 'b')
ax.text(H[0] + 0.1, H[1] + 0.1, 'H', fontsize=12, ha='center', color = 'b')
ax.text(K[0] + 0.1, K[1] - 0.2, 'K', fontsize=12, ha='center', color = 'b')
ax.text(Z[0] + 0.1, Z[1], 'z', fontsize=12, ha='center', color = 'b')
ax.text(Z2[0] - 0.1, Z2[1], 'z\'', fontsize=12, ha='center', color = 'b')

# Setting the plot
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel('')
ax.set_ylabel('')

plt.box(False)
plt.show()
