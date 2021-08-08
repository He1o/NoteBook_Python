import numpy as np


a = np.array([2, 3, 5])
b = np.array([6, 4, 3])
c = np.hstack((a,b))  #[2 3 5 6 4 3]


a = ['bobo']
b = ['aoao']
c = np.hstack(a,b)) #['bobo' 'aoao']
print(c)