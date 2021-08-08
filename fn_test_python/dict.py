bobo = {}
bobo['name'] = 'bobo'
bobo['age'] = 25
bobo['where'] = 'beijing'
bobo.clear()  #None  the first method


a = [['name','bobo'],['age',25],['where','bejing']]
bobo = dict(a)  #the second method
bobo.get('whos')  #None  get the values
bobo.get('name')  #get replace of index! allow access key that not exist

bobo.update({'name':'bobo&aoao'})  #if exist update the values
bobo.update({'heao':5})  #if not add them

items = list(bobo.items())
keys = list(bobo.keys())      #neet to call the list() function to 
values = list(bobo.values())  #convert them to a list
# [('name', 'bobo&aoao'), ('age', 25), ('where', 'bejing'), ('heao', 5)] 
# ['name', 'age', 'where', 'heao'] 
# ['bobo&aoao', 25, 'bejing', 5]
for i, j in bobo.items():
    print(i, j)
for i, j in list(bobo.items()):  #as the same  don't need list
    print(i, j)


a = bobo.pop('name')  #bobo
b = bobo.popitem()  #

bobo.setdefault('maths', 92)  #append a new key 'maths'
bobo.setdefault('age', 94)  #won't change the value of 'age'

dic = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
# print(dic)  #{'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'} 可直接打印字典

a = {'sdf':1, 'he':2, 'fd':3}
b = {value:name for name, value in a.items()}
print(b)  #{1: 'sdf', 2: 'he', 3: 'fd'}
# print(str(b))

a = {'sdf':1, 'he':2, 'fd':3}
b = {'sdf':1, 'he':2, 'fd':3}
print(a==b)
# 字典可以直接比较，相同keys和values则相同

a = {}
b = [1, 2, 3]
# a[b] = 0 #TypeError: unhashable type: 'list'
# 只有可以哈希的才能作为key， 列表、set、dict不可以
a[tuple(b)] = 0  #需要将列表转换为元组
a[1,2,3] = 0
# 可以分开输入，组合成元组

