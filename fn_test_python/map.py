bobo = [1, 2 ,3, 4, 5]

b = list(map(lambda x: x**2, bobo))
print(b)


b = list(map(float , bobo))  #对bobo中每个元素转换为float类型
print(b)
for a in map(float , bobo):  #map返回一个迭代器
    print(a)


