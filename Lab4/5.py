import numpy as np

A = np.array([[2, 3, 4, 1], [1, 2, 3, 4], [3, 4, 1, 2], [4, 1, 2, 3]])
A_det = np.linalg.det(A)
print(format(A_det, '.9g'))
