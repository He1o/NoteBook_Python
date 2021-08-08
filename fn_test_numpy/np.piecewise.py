import numpy as np

#分段的 

a = np.arange(20)
step = np.piecewise(a, [a>10, a<=10],
                        [lambda x: 20-x, lambda x:x])
print(step)
#  [ 0  1  2  3  4  5  6  7  8  9 10  9  8  7  6  5  4  3  2  1]