import numpy as np

a = np.array([[2,3,4],[5,6,7]])
b = a.ravel()
b[0] = 100

print(b)
print(a)  # will affect the original matrix 

a = np.array([[2,3,4],[5,6,7]])
b = a.flatten()
b[0] = 100

print(b)
print(a)