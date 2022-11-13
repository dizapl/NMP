from scipy.misc import derivative
import numpy as np
import math

def f(x):
    return pow(x,4) - 108*x + 7

eps = 0.0001

def nuton(a,b,eps):
    df2 = derivative(f, b, n = 2)
    if (f(b)*df2 > 0):
        xi = b
    else:
        xi = a
    df = derivative(f, xi, n = 1)
    xi_1 = xi - f(xi)/df
    while (abs(xi_1 - xi) > eps):
        xi = xi_1
        xi_1 = xi - f(xi)/df
    return print('Solving the equaton by Newton`s method x = ',xi_1)
nuton (-1, 3, eps)
nuton (3, 5, eps)
