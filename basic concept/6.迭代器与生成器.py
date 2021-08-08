# 可迭代对象
# 迭代器（iterator） 生成器（generator）
# 序列 字符串str 列表list 元组tuple 集合set
# 字典
# 如果一个对象拥有__iter__方法，其是可迭代对象，__iter__方法返回了一个迭代器对象
# 实际for语句的内部实现应该就是首先调用对象的__iter__方法，获取一个迭代器对象，接着不停的调用迭代器对象的__next__方法，循环遍历取值。
#!/usr/bin/env python
# coding=utf-8
class MyList(object):            # 定义可迭代对象类
 
    def __init__(self, num):
        self.data = num          # 上边界
 
    def __iter__(self):
        return MyListIterator(self.data)  # 返回该可迭代对象的迭代器类的实例
 
 
class MyListIterator(object):    # 定义迭代器类，其是MyList可迭代对象的迭代器类
 
    def __init__(self, data):
        self.data = data         # 上边界
        self.now = 0             # 当前迭代值，初始为0
 
    def __iter__(self):
        return self              # 返回该对象的迭代器类的实例；因为自己就是迭代器，所以返回self
 
    def __next__(self):              # 迭代器类必须实现的方法
        while self.now < self.data:
            self.now += 1
            return self.now - 1  # 返回当前迭代值
        raise StopIteration      # 超出上边界，抛出异常
 
my_list = MyList(5)              # 得到一个可迭代对象
# print(type(my_list))  #<class '__main__.MyList'>            # 返回该对象的类型  
my_list_iter = iter(my_list)     # 得到该对象的迭代器实例，iter函数在下面会详细解释
# print(type(my_list_iter))  #<class '__main__.MyListIterator'>
# for i in my_list:                # 迭代
    # print(i)  #[0,1,2,3,4]

# 迭代器
# 迭代器是一个可以记住遍历的位置的对象。
# 迭代器对象从集合的第一个元素开始访问，直到所有的元素被访问完结束。迭代器只能往前不会后退。
# 迭代器有两个基本的方法：iter() 和 next()。
# 字符串，列表或元组对象都可用于创建迭代器：

# 创建迭代器1
a = [3, 4, 5, 3, 7]
b = iter(a)
# print(b)  #<list_iterator object at 0x000001C948EDEF28>

# 创建迭代器2
# 把一个类作为一个迭代器使用需要在类中实现两个方法 __iter__() 与 __next__() 。
# __iter__() 方法返回一个特殊的迭代器对象， 这个迭代器对象实现了 __next__() 方法并通过 StopIteration 异常标识迭代的完成。
# __next__() 方法（Python 2 里是 next()）会返回下一个迭代器对象。

class MyNumbers:
  def __iter__(self):
    self.a = 1
    return self
 
  def __next__(self):
    if self.a <= 20:
      x = self.a
      self.a += 1
      return x
    else:
      raise StopIteration
 
myclass = MyNumbers()
myiter = iter(myclass)
# print(next(myiter))  1
# print(next(myiter))  2
# print(next(myiter))  3
# print(next(myiter))  4
# print(next(myiter))  5



# 生成器
# 在 Python 中，使用了 yield 的函数被称为生成器（generator）。
# 跟普通函数不同的是，生成器是一个返回迭代器的函数，只能用于迭代操作，更简单点理解生成器就是一个迭代器。
# 在调用生成器运行的过程中，每次遇到 yield 时函数会暂停并保存当前所有的运行信息，返回 yield 的值, 并在下一次执行 next() 方法时从当前位置继续运行。
# 调用一个生成器函数，返回的是一个迭代器对象。

# 创建生成器1
import sys
def fibonacci(n): # 生成器函数 - 斐波那契
    a, b, counter = 0, 1, 0
    while True:
        if (counter > n): 
            return
        yield a
        a, b = b, a + b
        counter += 1
f = fibonacci(10) # f 是一个迭代器，由生成器返回生成
 
# while True:
#     try:
#         print (next(f), end=" ")  #0 1 1 2 3 5 8 13 21 34 55
#     except StopIteration:
#         sys.exit()

# 创建生成器2
xx = [2,3,4,5]
h = (x*2 for x in xx)
print(h)  #<generator object <genexpr> at 0x000001F46ADB4138>
print(h.__next__())  #4