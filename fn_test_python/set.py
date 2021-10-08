#剔除重复元素后排序
'''
set集合 
setname = {element1,element2,...,elementn}
setname = set(iteration)  #不可变的数据类型，包括整形、浮点型、字符串、元组，
                           无法存储列表、字典、集合这些可变的数据类型

setname.add(element)  #添加元素
setname.remove(element)  #删除元素，没有对应元素会报错
setname.discard(element)  #删除元素，不会报错

set1 & set2  交集
set1 | set2  并集
set1 - set2  差集
set1 ^ set2  对称差集

listname.sort(reverse = true)  #倒序排列，永久性
sorted(listname)  #非永久性
'''

a=list(set(input()))
a.sort()
for i in a:
    print(i,end="")

a = input()
b = []
for i in a:
    if i not in b:
        b.append(i)
print(''.join(b))

str = "PL434-DIIEW"   #分割
if str.split("-",1)[0] == "PL434":
    str2 = "PL434"
    print(str2)

# "python.pythonPath": "D:\\ANACONDA\\envs\\GNN\\python.exe"