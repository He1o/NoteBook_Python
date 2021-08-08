from collections import defaultdict

# print(int())  #0
# print(list())  #[]
# print(dict())  #{}

#  当使用普通的字典时,用法一般是dict={},添加元素的只需要dict[element] =value即,调用的时候也是如此，dict[element] = xxx,但前提是element字典里，如果不在字典里就会报错
#  defaultdict的作用是在于，当字典里的key不存在但被查找时，返回的不是keyError而是一个默认值
dict1 = defaultdict(int)
dict1['he'] ='two'

print(dict1['ao'])  #  0

dict2 = defaultdict(list)
print(len(dict2['ww']) < 2)