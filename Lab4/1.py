
import numpy as np

A = np.array([[1, 2], [4, -1]])
B = np.array([[2, -3], [-4, 1]])
AB = A.dot(B)
BA = B.dot(A)
result = AB - BA
print(result)
