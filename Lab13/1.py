import math
import numpy as np
import matplotlib.pyplot as plt

def f(x, y):
    return x + math.cos(y / math.sqrt(11)) 

x0 = 2.1
b = 3.1
h = 0.1
x = np.arange(x0,b+h,h)
n = len(x) - 1
y = np.empty(n+1)
y[0] = 2.5

for i in range (n):
     y[i+1] = y[i] + h * f(x[i], y[i])

y_rounded = np.round_(y,4)
print('x =',x, '\ny =',y_rounded)

plt.plot(x,y,'o',x,y,'red')
plt.xlabel('x')
plt.ylabel('y')
plt.title('Метод Ейлера')
plt.legend(['точки','x+cos(y/sqrt(11))'])
plt.grid()
plt.show()
