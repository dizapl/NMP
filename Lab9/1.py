import matplotlib.pyplot as plt
from scipy.interpolate import UnivariateSpline
import numpy as np

x = [1.2, 1.4, 1.7, 2.3, 2.8]
y = [1.36, 1.15, 2.34, 0.92, 3.12]
spl = UnivariateSpline(x, y)
xs = np.linspace(1.2, 2.8, 1000)
plt.plot(x,y,'ro', xs, spl(xs), 'g')
plt.show()
