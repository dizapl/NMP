import numpy as np

A = np.array([[1, -5, 8, 9], [-2, 4, -3, -1], [7, -5, 6, -9]])
sum = 0
n = 0
value = 0
mid_value = 0

for i in range(3):
    for j in range(4):
        sum += A[i][j]
        n += 1
    value = sum / n
    if (value < mid_value):
        mid_value = value
    sum = 0
    n = 0
print('Найнижче середнє значення = ', mid_value)
