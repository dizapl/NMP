
import numpy as np
import math

def f(x):
    return x**4 - 108*x + 7

eps = 0.0001 

def rec_dyhotomy(a, b, eps):
    if abs(f(b)-f(a)) < eps:
        print('Корення немає')
        return

    mid = (a + b)/2
    if f(mid) == 0 or abs(f(mid)) < eps:
        print(f'Корінь знаходиться в точці х = {mid}')
    elif f(a)*f(mid) < 0:
        rec_dyhotomy(a, mid, eps)
    else:
        rec_dyhotomy(mid, b, eps)

rec_dyhotomy(-1, 3, eps)
rec_dyhotomy(3, 5, eps)
