import numpy as np

A = np.matrix('3, 2, 1; 2, -1, 1; 1, 5, 0')
print('A=',A)
B = np.matrix('5; 6; -3')
print('B=',B)

def kramer (A, B):
    a_det = np.linalg.det(A)
    print('Детермінант матриці = ', a_det)

    if (a_det != 0):
        print ('Розв*язуємо систему')
        x_m = np.matrix(A)
        x_m[:, 0] = B
        print('x_m=', x_m)
        y_m = np.matrix(A)
        y_m[:, 1] = B
        print('y_m=',y_m)
        z_m = np.matrix(A)
        z_m[:, 2] = B
        print('z_m=',z_m)
        x = np.linalg.det(x_m) / a_det
        y = np.linalg.det(y_m) / a_det
        z = np.linalg.det(z_m) / a_det
        print('X = ', round(x,5))
        print('Y=', round(y,5))
        print('Z=', round(z,5))
    else:
        print('Розв*язків немає')
kramer(A, B)

X = np.linalg.solve(A, B)
print('Перевірка X=',X)
