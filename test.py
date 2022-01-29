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
import sys
import time
def ProgressBar(current, total, bar_length = 50):
    hashes = '#' * int(current / total * bar_length)
    sys.stdout.write("\rPercent: [{}] %{}".format(hashes.ljust(bar_length, ' '), current))
    if current == total - 1:
        sys.stdout.write('\n')
    time.sleep(0.01)

for percent in range(0, 100):
    ProgressBar(percent, 100)
print(1111)
