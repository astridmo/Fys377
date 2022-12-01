import numpy as np
import math as m


def f(x):
    """Funksjonene dine"""
    f1 = 10*x[0] * m.sin(x[1]) + 2
    f2 = 10*x[0]**2 - 10*x[0]*m.cos(x[1]) + 1
    return np.array([f1, f2])


def jacobi_matrix(x):
    """Jacobimatrisen"""
    # Regner ut alle de partiellderiverte
    f1_x1 = 10 * m.sin(x[1])
    f1_x2 = 10 * x[0] * m.cos(x[1])
    f2_x1 = 20 * x[0] - 10 * m.cos(x[1])
    f2_x2 = 10 * x[0] * m.sin(x[1])
    return np.array([[f1_x1, f1_x2], [f2_x1, f2_x2]])


def newton_raphson(x, y, epsilon):
    epsilon_ny = np.ndarray([10, 10])  # dummy value
    i = 0

    while (epsilon_ny >= epsilon).any():
        delta_y = y - f(x)
        delta_x = np.linalg.solve(jacobi_matrix(x), delta_y)
        x_ny = x + delta_x
        try:
            epsilon_ny = abs((x_ny - x) / x)
        except ZeroDivisionError:
            epsilon_ny = np.array([10,10])
        x = x_ny
        i += 1
        if i > 10:
            print('LOL')
            break
        print(i)
    return x

x = [1, 0]
epsilon = 10**-4
y = np.array([0, 0])

print(newton_raphson(x, y, epsilon))