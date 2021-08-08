import numpy as np

b = np.array([[[1, 2], [2, 5], [3, 8]],
                [[1, 8], [2, 4], [3, 2]]])
print(np.shape(b))  #从外往内数 (2, 3, 2)

print(b.reshape(-1, 2))  #用-1自动计数，只需要给出列数自动计算行数
print(np.reshape(b, [-1, 2]))  #两种方式