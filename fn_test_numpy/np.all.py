import numpy as np

a = np.array([2, 3, 6])
b = np.array([2, 4, 6])
print(np.equal(a,b))  #[True False True]

print(np.all(np.equal(a,b)))  #False  
print(np.all(a == b))  #False 
#to determine if two matrices are completely equal