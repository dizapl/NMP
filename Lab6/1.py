import numpy as np
import matplotlib.pyplot as plt
from scipy.interpolate import lagrange

x=np.array([-1.,0.,1.,5.], dtype=float)
y=np.array([11.,4.,7.,-1.], dtype=float)

def lagranz(x,y,t):
    z=0

    for j in range(len(y)):
        p1=1; p2=1
        for i in range(len(x)):
            if i==j:
                p1=p1*1
                p2=p2*1
            else:
                p1=p1*(t-x[i])
                p2=p2*(x[j]-x[i])
        z=z+y[j]*p1/p2
    return z

xnew=np.linspace(np.min(x),np.max(x),100)
ynew=[lagranz(x,y,i) for i in xnew]
plt.plot(x,y,'o',xnew,ynew)
plt.title('Lagrange Polynomial_1')
plt.grid(True)
plt.show()

#Перевірка:
xnew=np.linspace(np.min(x),np.max(x),100)
ynew=[lagranz(x,y,i) for i in xnew]
f = lagrange(x, y)
fig = plt.figure(figsize = (10,8))

plt.plot(xnew, f(xnew), 'b', x, y, 'ro')
plt.title('Lagrange Polynomial_2')
plt.grid()
plt.xlabel('x')
plt.ylabel('y')
plt.show()

#Обчислення точок:
import numpy as np

x=np.array([-0.5, 2, 3, 4.5], dtype=float)
j = 0
for i in range(len (x)):
    y = - pow(x, 3) + 5 * pow(x, 2) - x + 4
    print ('x = ',x[i], 'y = ', y[j])
    j += 1
