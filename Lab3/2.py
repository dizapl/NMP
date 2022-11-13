from scipy.misc import derivative
import numpy as np
import math

def f(x):
    return pow(x,4) - 108*x + 7
eps = 0.0001

def komb(a,b,eps):
    if (derivative(f, a, n = 1)*derivative(f, a, n = 2)>0):
        a0 = a
        b0 = b
    else:
        a0 = b
        b0 = a
    ai = a0
    bi = b0
    while abs(ai-bi)>eps:
        ai_1 = ai -f(ai)*(bi - ai)/(f(bi) - f(ai))
        bi_1 = bi - f(bi)/derivative(f,bi, n= 1)
        ai = ai_1
        bi = bi_1
    x = (ai_1+bi_1)/2
    return print('Solving the equation by the combined method x = ', x)
komb(-1, 3, eps)
komb(3, 5, eps)
