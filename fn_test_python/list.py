import numpy as np

# 索引
a = np.mat([[1, 2, 2],[3, 6, 3]])  #必须加逗号
# print(a[[0, 1 ,0]])  #对矩阵进行数组索引，相当于提取对应的行数组成新矩阵[[1 2 2][3 6 3][1 2 2]]
a = [[1, 2, 2],[3, 6, 3]]
#print(a[[0, 1 ,0]])  #对列表list不能进行数组索引
a = [[2, 3, 4, 5, 6],[2, 3, 4, 5, 6]]
# print(a[0][2])  #注意list索引方式   #4
a = np.array([[2, 3, 4, 5, 6],[2, 3, 4, 5, 6]])
# print(a[0,2])  #array索引方式与list不同  #4  可以相同
a = np.array([[2],[3]])
b = list(a)
# print(a,b)   [[2] [3]]    [array([2]), array([3])]


# 列表运算
a = [3, 4]
a.append([2,1])
# print(a)  #[3, 4, [2, 1]]
a.extend([2,1])
# print(a)  #[3, 4, [2, 1], 2, 1]
b = a + [1]
# print(a)  #[3, 4, [2, 1], 2, 1]
# print(b)  #[3, 4, [2, 1], 2, 1, 1]
a *= 2
# print(a)  #[3, 4, [2, 1], 2, 1, 3, 4, [2, 1], 2, 1]
# print(b)  #[3, 4, [2, 1], 2, 1, 1]
a = [{'id': 9, 'type': 1}, {'id': 10, 'type': 1}]
b = [] + a
# print(b) #[{'id': 9, 'type': 1}, {'id': 10, 'type': 1}]
b = b + [{'id': 111, 'type': 22}]
# print(b) #[{'id': 9, 'type': 1}, {'id': 10, 'type': 1}, {'id': 111, 'type': 22}]


#列表推导
#在列表推导中不要使用两个以上表达式
#数据量较大时要用生成器表达式
b = [[] for _ in range(10)]
# print(b) #[[], [], [], [], [], [], [], [], [], []]
b = [[0,i] for i in range(10)]  
# print(b)  #[[0, 0], [0, 1], [0, 2], [0, 3], [0, 4], [0, 5], [0, 6], [0, 7], [0, 8], [0, 9]]
b.index([0,0])   #查找 0  找出第一个并不是所有
b = [[1000,i*100+50] for i in range(10)]
# print(b) 

a = [2, 3, 4, 3, 1, 3, 5]
b = [x**2 for x in a]  #[4, 9, 16, 9, 1, 9, 25]
b = [x**2 for x in a if x % 2 == 0]  #[4, 16] 过滤原列表中元素
#生成器表达式
b = (x**2 for x in a)  #<generator object <genexpr> at 0x00000277F26B4ED0>
c = next(b)  # 4
c = list(b)  #[9, 16, 9, 1, 9, 25] 会缺少第一项
print(c)


'''
# 切割操作

b = a[i:j] 表示复制a[i]到a[j-1]，以生成新的list对象
i缺省时默认为0,即 a[:n] 代表列表中的第一项到第n项，相当于 a[0:n]
j缺省时默认为len(alist),即a[m:] 代表列表中的第m+1项到最后一项，相当于a[m:5]
当i,j都缺省时，a[:]就相当于完整复制a
'''
a = [2, 3, 4, 2, 1, 3, 4, 5, 4]
b = a[:4]  #[2, 3, 4, 2]
b = a[3:]  #[2, 1, 3, 4, 5, 4]
b = a[-2:-1]  #[5]
b = a[-3:]  #[4, 5, 4]
b = a[:20]  #[2, 3, 4, 2, 1, 3, 4, 5, 4] 可以超出索引
b = a[-20:]  #[2, 3, 4, 2, 1, 3, 4, 5, 4]

'''
这里的s表示步进，缺省为1.（-1时即翻转读取）
所以a[i:j:1]相当于a[i:j]
当s<0时，i缺省时，默认为-1. j缺省时，默认为-len(a)-1
所以a[::-1]相当于 a[-1:-len(a)-1:-1]，也就是从最后一个元素到第一个元素复制一遍。
所以你看到一个倒序的东东。
'''
# 步进式切割  步进值（stride）
b = a[::2]  #[2, 4, 1, 4, 4] 每两个取一个值
b = a[::-2]  #[4, 4, 1, 4, 2]
b = a[::-1]  #[4, 5, 4, 3, 1, 2, 4, 3, 2] 翻转
a = '32334jhdiohg'
b = a[::-1]  #可用于翻转字符串！！

#  列表赋值时用切割操作，长度可以不等，列表会自动扩张或收缩
a[2:9] = ['a', 'e', 'w']  #[2, 3, 'a', 'e', 'w'] 
# print(a)

a=[1,2,3,4]
# print(a[8:10])
# 不会超出索引

hashmap = [[[0] * 9] * 9] * 3
hashmap = [[[0] * 9 for _ in range(9)]  for _ in range(3)]
# []*num  是浅复制 如果是元素的话没关系 如果是列表的话就不行
# 只能通过第二种方式创建多维数组