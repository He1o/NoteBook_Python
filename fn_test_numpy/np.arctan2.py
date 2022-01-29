import numpy as np
import matplotlib.pyplot as plt
# print(np.arctan2(1,1))
# print(np.pi/4)


# start = np.array([-100, -100])
# end = np.array([-50, 60])

# plt.scatter(start[0], start[1])
# plt.scatter(end[0], end[1])

# angle = np.arctan2(end[1] - start[1], end[0] - start[0])
# print(angle)
# f_att = np.array([100 * np.cos(angle), 100 * np.sin(angle)]) + start
# print(f_att)
# plt.scatter(f_att[0], f_att[1])
# plt.show()

x = [43.31096, -71.00215]
y = [43.31146, -71.00153]
angle = np.arctan2(-5, 5)
print(((angle / (2 * np.pi)) * 360 + 360) % 360)