
import numpy as np
import cmath

# Using (6.5.2) page 309

# ===========================
# Constants
# ===========================
y_1 = complex(0, 0)
y_2 = complex(0, 0)
z_12 = complex(0.05, 0.1)

V1 = complex(1, 0)
S_2 = complex(0.7, 0.4)

y_12 = 1/z_12

# =============================
# Admittansmatrise
# =============================
Y_11 = y_1 + y_12
Y_21 = -y_12
Y_12 = -y_12
Y_22 = y_2 + y_12

Y = [[Y_11, Y_12], [Y_21, Y_22]]
print(Y)

# =============================
# Calculate V2
# =============================
V2 = complex(1, 0)  # Start value


def gausseidel_easy(Y_22, S_2, V2, Y_21, V1):
    V2 = (1/Y_22) * ((np.conj(S_2)/np.conj(V2)) - (Y_21 * V1))
    return V2

V2_it1 = gausseidel_easy(Y_22, S_2, V2, Y_21, V1)
V2_it2 = gausseidel_easy(Y_22, S_2, V2_it1, Y_21, V1)
V2_it3 = gausseidel_easy(Y_22, S_2, V2_it2, Y_21, V1)


print('Svaret er:', cmath.polar(V2_it1), cmath.polar(V2_it2), cmath.polar(V2_it3))
