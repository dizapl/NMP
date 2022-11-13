
import numpy as np
import math
from scipy.misc import derivative

def f(x):
    return 6*pow(x,4) +4*pow(x,3) - pow(x,2) - x - 10

eps = 0.001 #точність

def hord (a, b, eps):
    if (f(a)*derivative(f, a, n = 2)>0):
        x0 = a
        xi = b
    else:
        x0 = b
        xi = a

    xi_1 = xi-(xi - x0) * f(xi)/(f(xi) - f(x0))
    while (abs(xi_1 - xi) > eps):
        xi = xi_1
        xi_1 = xi-(xi - x0) * f(xi)/(f(xi) - f(x0))
    else:
        print(f'Метод хорд.Корінь знаходиться в точці x =', round(xi_1,5))

hord(-1,3,eps)
hord(3,5,eps)