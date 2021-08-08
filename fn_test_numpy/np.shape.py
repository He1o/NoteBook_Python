import numpy as np

a = np.array([[1, 2, 2]])
print(np.shape(a))

b = np.array([[[1], [2], [3]],[[1], [2], [3]]])
print(np.shape(b))  #从外往内数 (2, 3, 1)

c = [[[1], [2], [3]],[[1], [2], [3]]]
print(np.shape(c))  #np里的数组与Python数组似乎没有区别，可以同样处理 (2, 3, 1)

print(type(a),type(b),type(c)) #<class 'numpy.ndarray'> <class 'numpy.ndarray'> <class 'list'> 类型显示是不同的


