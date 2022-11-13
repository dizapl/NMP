import numpy as np
from scipy import optimize
from scipy.misc import derivative
import math

x0 = 1.3
y0 = -1.7
def f1(y):
    return -1*math.cos(y - 2) + 0.5

def f2 (x):
    return math.sin(x + 2) - 1.5

def iter (x,y,e):
    xn = x
    yn = y
    xn1 = f2(x)
    yn1 = f1(y)
    n = 1
    while ((abs(xn1-xn)>=e) & (abs(yn1-yn) >=e)):
        xn = xn1
        yn = yn1
        xn1 = f2(yn)
        yn1 = f1(xn)
        n += 1
    print ('Simple iteration:')
    print ('x=', xn, '\ny=',yn,'\nThe amount of iteration = ',n)
iter(x0,y0,0.0001)
