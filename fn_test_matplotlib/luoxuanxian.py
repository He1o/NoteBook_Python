import matplotlib.pyplot as plt
import numpy as np
for t in range(1,1000):
    s = 200-2*t/10 
    angle = t/1000 * 10 * np.pi
    x = s*np.cos(angle)
    y = s*np.sin(angle)
    plt.scatter(x,y)
plt.axis([-200, 200, -200, 200])
plt.show()