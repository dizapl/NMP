import numpy as np

A = np.array([[1, 2, -3], [0, 1, 2], [0, 0, 1]])
A_inv = np.linalg.inv(A)
print(A_inv)
