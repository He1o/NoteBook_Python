import numpy as np

a = [2, 4, 5]       #(3,)
b = [[2] , [3], [4]]#(3, 1)
c = [4, 5, 6]       #(3,)
d = [[2, 3, 4],     #(2, 3)
     [3, 4, 5]]
print(np.dot(a,b))  #[36]
print(np.dot(a,c))  #58
print(np.dot(d,a))  #[36 47]
print(np.array(a)*np.array(c))  #[8 20 30]
print(np.shape([3])) #(1,)
print(np.shape(3)) #()