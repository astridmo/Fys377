
import numpy as np


def gausseidel(A, x, y, epsilon):
    D = np.tril(A)  # Diagonal matrix
    Dinv = np.linalg.inv(D)  # Inverse of matrix D
    M = np.matmul(Dinv, (D - A))
    i = 1

    def _rekke(x, i):
        """Recursion as long as the error>limit"""
        x_ny = np.matmul(M, x) + np.matmul(Dinv, y)
        if (abs(x_ny - x)/abs(x) >= epsilon).any():
            i += 1
            print(i)
            x = _rekke(x_ny, i)
        return x

    x_answ = _rekke(x, i)
    return x_answ

A = np.array([[8, 2, 1], [4, 6, 2], [3, 4, 14]])
x = np.array([0, 0, 0])
epsilon = 0.01
y = np.array([3, 4, 2])

print(gausseidel(A, x, y, epsilon))