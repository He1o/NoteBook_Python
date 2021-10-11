import random
import numpy as np


# a = list(range(10))
# b = np.random.shuffle(a)
# print(a)
# a = np.array([3.76871427e+00, 8.09434346e-01, 5.75109625e+00, 1.38175360e+00])
# print(np.ceil(a).astype(np.int))
# # a[[0,2,1]]
# print(a[[3,2,1]])
# # b = np.argsort(a[[3,2,1]])
# # print(b)
# print(zip([3,2,1], a[[3,2,1]]))
# a = sorted(zip([3,2,1], a[[3,2,1]]), key=lambda x: x[1])
# print(a)

# print(np.sqrt(np.sum((np.array((2,3))-np.array((3,3)))**2)))
# print(np.inf +1)
# x, y =2, 3
# print(x, y)

# print(np.argmin([2,3,5,1,2]))

# a = np.array([[1, 2, 3, 4], [1, 2, 3, 4]])
# b = np.array([[3, 4, 5, 6], [3, 4, 5, 6]])
# np.clip(a, 2, 3)
# a[1] = b[0]
# print(a)


a = np.array([2,3,3,4])
print(a[np.array([2,3])])
print(5e3)

x = {2:[3,4,4,5],4:[6,7,8]
}
sorted(x.items(), key = lambda x: len(x))
print(sorted(x.items(), key = lambda x: len(x[1])))