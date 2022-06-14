import numpy as np

x = np.array([1, 2, 3, 4])
x

A = np.array([[1,2],[3,4],[5,6]])

type(A)

A.shape

x.shape

len(x)

A_T = A.T

A_T = A.transpose()

A_T.shape

B = np.array([[2, 5], [7, 4], [4, 3]])
B

C = A + B 
print (C)

A = np.array([[1, 2], [3, 4], [5, 6]])
B = np.array([[2], [4]])
print (C)
C = A.dot(B)
C
print (C)
I = np.eye(3)
print (I)
IA = I.dot(A)
IA
print (IA)

M = np.array([[1,2],[3,4]])
M
print (M)
M = np.array([[1,2],[3,4]])
det_M = np.linalg.det(M)
det_M
print (M)

A = np.array([[3, 0, 2], [2, 0, -2], [0, 1, 1]])
print (A)
A_inv = np.linalg.inv(A)
A_inv
print (A_inv)
I = A_inv.dot(A)
print (I)