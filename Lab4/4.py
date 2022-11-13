import numpy as np

A = np.array([[1, 2, 3], [-1, 2, 1], [1, 3, 2]])
result = np.linalg.det(A)
print(format(result, '.9g'))
