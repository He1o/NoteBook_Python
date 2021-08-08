a = [1, 2, 3]
b = [2, 3 ,4]
c = zip(a,b)  #zip是个函数，返回的是一个zip object
print(c)

lt4 = ['bobo','18','183']
lt5 = ['name','age','height']
a = zip(lt5,lt4)
print(list(a))  #[('name', 'bobo'), ('age', '18'), ('height', '183')] 元素是元组

lt4 = ['bobo','18','183']
lt5 = ['name','age','height']
a = zip(lt5,lt4)
print(dict(a))  #{'name': 'bobo', 'age': '18', 'height': '183'} 转换成字典

bound = [[2,4], [3,4]]
print(list(zip(*bound)))  #[(2, 3), (4, 4)]  相当于zip([2,4], [3,4])

print(list(zip([2,3])))  #[(2,), (3,)]  可以zip一个单位



a =  [[2, 4, 3], [3, 4, 4], [3, 4, 4]]
b,c,d = list(zip(*a))
print(b)
