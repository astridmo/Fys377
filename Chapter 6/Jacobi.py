import numpy as np

M = np.array([[0, -0.25, -1/8], [-2/3, 0, -1/3], [-3/14, -2/7, 0]])
A = np.array([[8, 2, 1], [4, 6, 2], [3, 4, 14]])
y = np.array([3, 4, 2])

diag = np.diag(A)
D = np.zeros((3, 3), float)
np.fill_diagonal(D, diag)

Dinv = np.linalg.inv(D)  # Inverse of matrix D

# Start value of x
x = np.array([0, 0, 0])

epsilon = 10**-4

print(M)

for _ in range(10):
    x = np.matmul(M, x) + np.matmul(Dinv, y)

print(x)
