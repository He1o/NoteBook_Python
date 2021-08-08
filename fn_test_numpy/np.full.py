import numpy as np

a = np.full((10,10),fill_value = np.inf)

print(np.argmax(a[-11][0]))