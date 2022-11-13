import numpy as np
from math import factorial

x=[0.45, 0.46, 0.47, 0.48, 0.49, 0.50, 0.51, 0.52, 0.53, 0.54, 0.55]
y=[20.1946, 19.6133, 18.9425, 18.1746, 17.3010, 16.3123, 15.1984, 13.9484, 12.5508, 10.9937, 9.2647]
h = x[1] - x[0]
x1=0.455
x2=0.533

q=(x1 - x[0])/h
q1 = (x2-x[-1])/h

def n(y,j):
    mas=[]
    for i in range(len(y)):
        mas.append(y[i] - y[i-1])
    mas.pop(0)
    if j == 1:
        return mas
    else:
        j-=1
        return n(mas, j)
        
#Перша інтерполяційна формула Ньютона
s_1 = y[0]+q*n(y,1)[0]+q*(q-1)*n(y,2)[0]/factorial(2)
s_2 = q*(q-1)*(q-2)*n(y,3)[0]/factorial(3)
s_3 = q*(q-1)*(q-2)*(q-3)*n(y,4)[0]/factorial(4)
s_4 = q*(q-1)*(q-2)*(q-3)*(q-4)*n(y,5)[0]/factorial(5)
n_1 = s_1 + s_2 + s_3 + s_4
print ('The value of a function at a point x1=', x1, 'using Newton*s First Interpolation Formula', round(n_1,5))

#Друга інтерполяційна формула Ньютона
s_1 = y[10]+q1*n(y,1)[9]+q1*(q1+1)*n(y,2)[8]/factorial(2)
s_2 = q1*(q1+1)*(q1+2)*n(y,3)[7]/factorial(3)
s_3 = q1*(q1+1)*(q1+2)*(q1+3)*n(y,4)[6]/factorial(4)
s_4 = q1*(q1+1)*(q1+2)*(q1+3)*(q1+4)*n(y,5)[5]/factorial(5)
n_2 = s_1 + s_2 + s_3 + s_4
print ('The value of a function at a point x2=', x2, 'using Newton*s Second Interpolation Formula', round(n_2,5))
