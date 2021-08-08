import numpy as np

x = np.power([2,3,4] , 2)  #[4 9 16]
y = np.power([2,3,4] , 2)
a = [1, 1]
b = (np.power(x - a[0], 2) + np.power(y - a[1], 2))
print(b)

print(np.array([2,3,4])**2)
