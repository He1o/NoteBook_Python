import numpy as np

x_data = np.linspace(1, 50)  #默认插值一共50个点
x_data = np.linspace(1, 50, 10)
print(x_data)

b_data = list(range(10, 15))  #左闭右开，返回的是一个obj
print(b_data)

x_data = np.linspace(50, 20, 6)
print(x_data)
