import numpy as np

a = np.array([1, 2, 2])
b = [1, 3, 9]
# print(a + b)  #np里的array可以与Python中的列表相加  [ 2  5 11]

#  print(a[0,0])  数组不能用[0,0]索引，只有一个维度

a = np.array([[1, 2, 2],[3, 6, 3]])  #必须加逗号
# print(a[[0, 1 ,0]])  #对数组进行数组索引，相当于提取对应的行数组成新矩阵[[1 2 2][3 6 3][1 2 2]]

# print(a[:,-2:])  # 取每行的最后两个
# print(a[:,:2])  # 取每行的前两个

for i, j in enumerate(a):
    for c, d in enumerate(j):
        pass
        # print(i, c, d)
# 0 0 1
# 0 1 2
# 0 2 2
# 1 0 3
# 1 1 6
# 1 2 3


# print(a[(1,1)])  # 6
# print(np.array((2,3)))  # [2 3]
# print(np.array([2,3]))  # [2 3]

a = [[2], [3], [4], [5]]
a = np.array(a)
# print(a[[2,2]])  # [[4] [4]]
# print(a[1][0])  # 3

a = np.array([2, 3, 4, 3])
b = a - 1
print(b)  #[1 2 3 2]

b = 0
a[np.nonzero(a>2)] = 2
b += a
print(b)

a = np.array([0,0])
a += [8,9]
a += [2,3]
print(a)

a = np.array([[0,0],[3,3]])
a[0,:] = 2,3
print(a)