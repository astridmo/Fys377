import numpy as np


def jacobi(A, x, y, epsilon):
    D = np.diag(np.diag(A))  # Diagonal matrix
    Dinv = np.linalg.inv(D)  # Inverse of matrix D
    M = np.matmul(Dinv, (D - A))
    i = 0

    def _rekke(x, i):
        """Recursion as long as the error>limit"""
        x_ny = np.dot(M, x) + np.dot(Dinv, y)
        i += 1
        print(i)
        if (abs((x_ny - x)/x) >= epsilon).any():
            x_ny = _rekke(x_ny, i)
        return x_ny

    x_answ = _rekke(x, i)
    return x_answ

# M = np.array([[0, -0.25, -1 / 8], [-2 / 3, 0, -1 / 3], [-3 / 14, -2 / 7, 0]])
A = np.array([[8, 2, 1], [4, 6, 2], [3, 4, 14]])
y = np.array([3, 4, 2])

# diag = np.diag(A)
# D = np.zeros((3, 3), float)
# np.fill_diagonal(D, diag)
#
# Dinv = np.linalg.inv(D)  # Inverse of matrix D

# Start value of x
x = np.array([0, 0, 0])

epsilon = 0.01

# for _ in range(50):
#     x = np.matmul(M, x) + np.matmul(Dinv, y)

# print('FASIT', x)

A = np.array([[8, 2, 1], [4, 6, 2], [3, 4, 14]])
x = np.array([0, 0, 0])

print('********\nOppgave 6.6:\n', jacobi(A, x, y, epsilon))

# ============================================
# Oppgave 6.8
# ============================================
A_8 = [[10, -2, -4], [-2, 6, -2], [-4, -2, 10]]
y_8 = [-2, 3, -1]
x_8 = [1, 1, 0]
epsilon_8 = 0.05
print('********\nOppgave 6.8:\n', jacobi(A_8, x_8, y_8, epsilon_8))