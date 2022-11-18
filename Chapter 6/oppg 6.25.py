import math as m
from sympy import *


def f(x):
    f1 = 10*x[0] * m.sin(x[1]) + 2
    f2 = 10*x[0]**2 - 10*x[0]*m.cos(x[1]) + 1
    return f1, f2


