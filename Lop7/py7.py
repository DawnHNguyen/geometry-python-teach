import matplotlib.pyplot as plt
import numpy as np

fig, ax = plt.subplots()

angle = 20
side1 = 6
side2 = 8.5

direction = np.array([np.cos(np.radians(angle)), np.sin(np.radians(angle))])

B = np.array([-10, 0])
C = np.array([-10 + side1, 0])
A = B + direction * side2

N = np.array([0, 0])
P = np.array([side1, 0])
M = N + direction * side2

ax.plot([A[0], B[0]], [A[1], B[1]], 'green', linewidth=2)
ax.plot([A[0], C[0]], [A[1], C[1]], 'blue', linewidth=2)
ax.plot([B[0], C[0]], [B[1], C[1]], 'red', linewidth=2)

ax.plot([M[0], N[0]], [M[1], N[1]], 'green', linewidth=2)
ax.plot([M[0], P[0]], [M[1], P[1]], 'blue', linewidth=2)
ax.plot([N[0], P[0]], [N[1], P[1]], 'red', linewidth=2)

ax.text(A[0], A[1] + 0.1, 'A', fontsize=12, ha='center', color = 'k')
ax.text(B[0], B[1] + 0.1, 'B', fontsize=12, ha='center', color = 'k')
ax.text(C[0] + 0.5, C[1] + 0.1, 'C', fontsize=12, ha='center', color = 'k')
ax.text(M[0], M[1] + 0.1, 'M', fontsize=12, ha='center', color = 'k')
ax.text(N[0], N[1] + 0.1, 'N', fontsize=12, ha='center', color = 'k')
ax.text(P[0] + 0.5, P[1] + 0.1, 'P', fontsize=12, ha='center', color = 'k')

# Setting the plot
ax.set_xticks([])
ax.set_yticks([])
ax.set_xlabel('')
ax.set_ylabel('')
ax.set_aspect('equal')

plt.box(False)
plt.show()