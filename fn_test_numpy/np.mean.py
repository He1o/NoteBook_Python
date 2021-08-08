import numpy as np

c = [[[1], [2], [3]],[[1], [2], [3]]]
print(np.mean(c))
print(np.mean(c, axis = 0))
print(np.mean(c, axis = 1))
print(np.mean(c, axis = 2))

a = np.mat([[1, 2, 2],[3, 6, 3]]) 
print(np.mean(a))
print(np.mean(a, axis = 0))
print(np.mean(a, axis = 1))

a = np.array([[1, 2, 2],[3, 6, 3]]) 
print(np.mean(a))
print(np.mean(a, axis = 0))
print(np.mean(a, axis = 1))

'''
2.0
[[1.]
 [2.]
 [3.]]
[[2.]
 [2.]]
[[1. 2. 3.]
 [1. 2. 3.]]

2.8333333333333335
[[2.  4.  2.5]]
[[1.66666667]
 [4.        ]]

2.8333333333333335
[2.  4.  2.5]
[1.66666667 4.        ]
'''