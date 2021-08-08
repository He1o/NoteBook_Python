# 在Python中，对对象有一种很通俗的说法，万物皆对象。
# 说的就是构造的任何数据类型都是一个对象，无论是数字、字符串、还是函数，
# 甚至是模块、Python都对当做对象处理。
# 所有Python对象都拥有三个属性：身份、类型、值。


a = 3
b = a
b = 2
# print(a, b)  #3 2   深层复制

a = [2,3]
b = a
b = [1,2]
# print(a, b)  #[2, 3] [1, 2]

a = [2,3]
b = a
b[0] = [1,2]
# print(a, b)  #[[1, 2], 3] [[1, 2], 3]  浅复制

a = [[2], [3]]
print(a)
b = [i for i in a]
print(b)
b[0][0] = 4
print(a)  #[[4], [3]]  浅复制
print(b)

# 列表深层复制方法
a = [2, 3, 4, 5]
b = a[:]
a[0] = 100
print(b)