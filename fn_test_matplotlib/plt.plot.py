import matplotlib.pyplot as plt

squares = [1, 4, 9, 16, 25]
plt.plot(squares)  #无需x轴信息 从0开始
plt.savefig('D:\\Python_new\\Python_test\\fn_test_matplotlib\\he.png')
input_values = [1, 2, 3, 4, 5]
plt.plot(input_values, squares, linewidth = 5)
plt.savefig('.\\he2.png')

# 设置图表标题，并给坐标轴加上标签 fontsize字体大小
plt.title("square numbers", fontsize = 24)
plt.xlabel("value", fontsize = 14)
plt.ylabel("square of value", fontsize = 14)
#  设置刻度标记的大小
plt.tick_params(axis = 'both', labelsize = 14)
# plt.show()