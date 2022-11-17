import copy

import numpy as np

# Using (6.5.2) page 309

x = [1, 1]
x_ny = [2, 2]
epsilon = 0.05
i = 0

epsilon_ny1 = abs((x_ny[0] - x[0])/x[0])
epsilon_ny2 = abs((x_ny[1] - x[1])/x[1])


while epsilon_ny1 >= epsilon or epsilon_ny2 >= epsilon:
    x_ny[0] = 1/complex(0, -20) * (complex(-1, 0.5)/np.conj(x[0]) - complex(0, 10) * x[1] - complex(0, 10))
    x_ny[1] = 1/complex(0, -20) * (complex(-3, 1)/np.conj(x[1]) - complex(0, 10) * x_ny[0] - complex(0, 10))
    epsilon_ny1 = abs((x_ny[0] - x[0])/x[0])
    epsilon_ny2 = abs((x_ny[1] - x[1]) / x[1])
    x = x_ny.copy()

    i += 1
    if i == 10:
        print('lol, du divergerer')
        break


print(x_ny)
print(i)
