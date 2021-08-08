# 类 Class Objects
# 类拥有两种操作,
# 1.类属性 attribute references 
# 2.实例化instantiation
# 类属性就相当于专属于一个类的变量(即某些语言中的类的静态公共变量static public),使用方法是:类名称.类属性名称
# 实例化则是创建一个类的实例的方法,使用方法是:类名称()
# 在使用实例化方法后,将会创建一个空的类实例,一般的python类的定义中会有一个特殊的方法来初始化,这个方法就是__init__(),当调用了类的实例化方法后,__init__()方法会立刻被这个类的实例调用.也就是说,__init__()不是构造函数,而是一个普通的方法.

# 类的实例 Instance Objects
# 类的实例只拥有一种操作,这就是 1.属性调用 attribute references.
# 属性调用指 1.数据属性 2.方法
# 数据属性
# 数据属性不需要预先定义!当数据属性初次被使用时,它即被创建并赋值(they spring into existence when they are first assigned to)

# 在python的class中有两种属性:类属性,数据属性.(大多数编程语言都有这样两种属性).类属性属于类,数据属性属于类的实例.
# 改变类属性，看上去实例属性跟着变，事实上那并不是实例属性，只是通过实例来访问的类属性，实例属性和类属性是分开的，如果实例属性命名和类属性相同，会先隐藏掉类属性。
# 访问类属性是用 类名.attr ;访问实例属性时用 实例名.attr 。实例可以访问类属性，但是类不能访问实例属性。
class bobo():
    def __init__(self):
        self.a = 1

    def add(self):
        self.a += 1

    def lll(self):
        b = self.a = 10
        return b


bo = bobo()
co = bobo()
bo.add()
print(bo.lll())
print(bo.a,co.a)  #实例相互独立，值不同