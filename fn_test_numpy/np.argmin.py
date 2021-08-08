import numpy as np
distance = [np.inf for _ in range(10)]
print(distance)
distance[5] = 1

print(np.argmin(distance,0))