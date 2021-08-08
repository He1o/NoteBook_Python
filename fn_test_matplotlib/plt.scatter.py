import matplotlib.pyplot as plt

plt.scatter(2, 4, s = 200)  #s调节点的尺寸


x_values = list(range(1, 1001))
y_values = [x**2 for x in x_values]
plt.subplot(221)
plt.scatter(x_values, y_values, c = 'red', s = 4)  #通过c改变颜色

plt.subplot(222)
plt.scatter(x_values, y_values, c = (0, 0, 0.8), s = 4)  #（0，0, 0）是黑色

plt.subplot(223)
plt.scatter(x_values, y_values, c = y_values,  s = 40)
plt.axis([0, 1100, 0, 1100000])  #设置坐标轴范围
plt.show()

plt.savefig('squares_plot.png', bbox_inches = 'tight')  #保存文件
