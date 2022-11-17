import copy


def f(x):
    """The function"""
    return x**3 + 8*x**2 + 2*x - 40


def J(x):
    """Jacobi matrix. The derivative of f(x)"""
    return 3*x**2 + 16*x + 2

def calc_epsilon(x_ny, x):
    return abs((x_ny - x)/x)

y = 0
x = 1  # Start value
epsilon = 0.001
x_ny = 4
new_epsilon = 1000  # dummy value
i = 0

while new_epsilon >= epsilon:
    x_ny = x + J(x) ** -1 * (y - f(x))
    new_epsilon = calc_epsilon(x_ny, x)
    x = copy.copy(x_ny)
    print(x)
    i += 1

print(i)
