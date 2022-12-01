import numpy as np
import cmath

Y_kk = complex(0, -10)
Y_12_21 = complex(0, 5)
Y_13_31 = complex(0, 5)
Y_23_32 = complex(0, 5)

Y_bus = [[Y_kk, Y_12_21, Y_13_31],
         [Y_12_21, Y_kk, Y_23_32],
         [Y_13_31, Y_23_32, Y_kk]]


V_start = complex(1, 0)
V_0 = [V_start, V_start, V_start]
S = [0, complex(-1, -0.5), complex(-1.5, -0.75)]


def gauss_seidel(Y_kk, S, V):
    V_ny = V.copy()
    # Oppdaterer V2
    V_ny[1] = (1/Y_kk) * (np.conj(S[1])/np.conj(V[1]) - Y_12_21 * V[0] - Y_23_32 * V[2])
    # Oppdaterer V3
    V_ny[2] = (1/Y_kk) * (np.conj(S[2])/np.conj(V[2]) - Y_13_31 * V[0] - Y_23_32 * V_ny[1])
    return V_ny


V_1 = gauss_seidel(Y_kk, S, V_0)
V_2 = gauss_seidel(Y_kk, S, V_1)

print('Iterasjon 1 er: \nV2: ', cmath.polar(V_1[1]), '\nV3: ', cmath.polar(V_1[2]))
print('Iterasjon 2 er: \nV2: ', cmath.polar(V_2[1]), '\nV3: ', cmath.polar(V_2[2]))
