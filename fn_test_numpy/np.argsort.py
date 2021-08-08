import numpy as np

a = np.array([3,4,24,435,1,45,7,np.inf])

b = a.argsort()  #[4 0 1 6 2 5 3 7]
# print(b)

a = a.reshape((2,4))
b = a.argsort(axis=0)   #[[1 0 1 0]  [0 1 0 1]]

# print(b)  
b = a.argsort(axis=1)   #[[0 1 2 3] [0 2 1 3]]
print(b)