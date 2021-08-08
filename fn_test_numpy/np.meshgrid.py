import numpy as np
# import matplotlib.pyplot as plt

x = [2, 4, 9]
y = [3, 5, 6, 8]

X, Y = np.meshgrid(x, y)  #3*4 points 
#[2,4,9] [3,3,3]   x-coordinate and y-coordinate
#[2,4,9] [5,5,5]   x-coordinate and y-coordinate
print(X,Y)
# plt.plot(X, Y,
#          color='limegreen',  # 设置颜色为limegreen
#          marker='.',  # 设置点类型为圆点
#          linestyle='')  # 设置线型为空，也即没有线连接点
# plt.grid(True)
# plt.show()
