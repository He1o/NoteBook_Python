'''1. 序列解包'''
# 利用*获取单个变量中的多个元素！！
a,b,*c = (1,2,3,4,5,6)
print(a,b,c)  #1 2 [3, 4, 5, 6]

a,b,*c = 'skdjfwpe'
print(a,b,c)  #s k ['d', 'j', 'f', 'w', 'p', 'e']  获取剩余部分

a,*b,c = (1,2,3,4,5,6)
print(a,b,c)  #1 [2, 3, 4, 5] 6  获取中间部分

a,*b,c = (1,2) 
print(a,b,c)  #1 [] 2  如果左值比右值要多，那么带 * 的变量默认为空

(a, b), (c, d) = (1, 2), (3, 4)
print(a,b,c,d)  

# 元组解包
print((*(2,3), 3))  #(2, 3, 3)
'''2. 函数形参'''
# *args 和 **kwargs 主要用于函数定义。
# 你可以将不定数量的参数传递给一个函数。不定的意思是：预先并不知道, 函数使用者会传递多少个参数给
# 你, 所以在这个场景下使用这两个关键字。其实并不是必须写成 *args 和 **kwargs。  *(星号) 才是必须
# 的. 你也可以写成 *ar  和 **k 。而写成 *args 和**kwargs 只是一个通俗的命名约定。
# python函数传递参数的方式有两种：
# 位置参数（positional argument）
# 关键词参数（keyword argument）
# *args 与 **kwargs 的区别，两者都是 python 中的可变参数：
# *args 表示任何多个无名参数，它本质是一个 tuple
# **kwargs 表示关键字参数，它本质上是一个 dict
# 如果同时使用 *args 和 **kwargs 时，必须 *args 参数列要在 **kwargs 之前。
# arguments keywordsarguments

def fun(*args, **kwargs):
    print(args)
    print(kwargs)
fun((1,2,3,4),A = 1, b = 2, c = 4) #((1, 2, 3, 4),) {'A': 1, 'b': 2, 'c': 4}
fun(1, 2, 3, 4, A = 1, b = 2, c = 4)  #(1, 2, 3, 4) {'A': 1, 'b': 2, 'c': 4}
# 分别形成一个元组和字典

def fun2(name, *args, **kwargs):
    print('hello', name)
    for arg in args:
        print('你的朋友', arg)
    for key, value in kwargs.items():
        print('{} 喜欢 {}'.format(key, value))
fun2("Geek", "dog", "cat", Geek="cat", cat="box")

# hello Geek
# 你的朋友 dog
# 你的朋友 cat
# Geek 喜欢 cat
# cat 喜欢 box

def fun3(name, *, Geek="cat", cat="box"):  # *之后的参数只能用关键字参数，不能用位置参数
    print('hello', name)
    print('{} 喜欢 {}'.format('Geek', Geek))
# fun3("Geek", "aa", "bb", )  #TypeError: fun3() takes 1 positional argument but 3 were given
fun3("Geek",Geek= "aa",cat= "bb", )

'''3. 函数实参'''
# 如果函数的形参是定长参数，也可以使用 *args 和 **kwargs 调用函数，类似对元组和字典进行解引用：

def fun3(data1, data2, data3):
    print('data1', data1)
    print('data2', data2)
    print('data3', data3)
args = ('he',2,'ao')
# args = ['he', 3, 'ao']  #列表、元组都可以
fun3(*args)
# data1 he
# data2 2
# data3 ao

# 字典key必须与函数的形参名对应
kwargs = {'data2':1 , 'data3':2,'data1':3}
fun3(**kwargs)
# data1 3
# data2 1
# data3 2


