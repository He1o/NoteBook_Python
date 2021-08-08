def f2():
    list1 = []
    for i in range(5):
        def n(x):
            return i+x
        list1.append(n)
    return list1
mylist = f2()
for i in mylist: print(i)
print(mylist[0](2))
print(mylist[2](2))

# <function f2.<locals>.n at 0x000001FC7B23CD08>
# <function f2.<locals>.n at 0x000001FC7B23CD90>
# <function f2.<locals>.n at 0x000001FC7B23CE18>
# <function f2.<locals>.n at 0x000001FC7B23CEA0>
# <function f2.<locals>.n at 0x000001FC7B23CF28>
# 6
# 6

def f1():
    for i in range(5):
        def n():
            print(i)
    return n
f1()()  #4

# 结果输出4。可见，print(i)的值并没有随循环的迭代过程而改变。
# 究其原因，是因为def n()只是函数的声明，它不会去查找i的值是多少，所以不会将i的值替换到函数n()的i变量，而是直接保存变量i的地址，当循环结束时，i指向最后一个元素i=4的地址。
# 当开始调用n()的时候，即f1()()，才会真正开始查找i的值，这时候i指向的正是i=4。

# 如果要保证循环的迭代能作用到其内部的函数中，可以采用默认参数值的方式进行赋值：
def f3():
    list1 = []
    for i in range(5):
        def n(x,i=i):
            return i+x
        list1.append(n)
    return list1
# 上面def n(x,i=i)中的i=i是设置默认参数值，等号右边的i是函数声明时就查找并替换完成的，所以每次循环迭代过程中，等号右边的i都不同，等号左边的参数i的默认值就不同。



# 首先给出闭包函数的必要条件：
# 闭包函数必须返回一个函数对象,闭包函数返回的那个函数必须引用外部变量（一般不能是全局变量），而返回的那个函数内部不一定要return

# 嵌套函数line中的代码访问了a和b变量，line本身函数体内并不存在这两个变量，所以会逐级向外查找，往上走一层就找到了来自主函数line_conf传递的a, b。若往外直至全局作用域都查找不到的话代码会抛异常。
def line_conf2(a, b):
    def line(x):
        return a * x + b
 
    return line
# 定义两条直线
line_A = line_conf2(2, 1)  # y=2x+b
line_B = line_conf2(3, 2)  # y=3x+2
# 打印x对应y的值
print(line_A(1))  # 3
print(line_B(1))  # 5


def line_conf():
    a = 1
    b = 2
    def line(x):
        print(a * x + b)
    return line
L = line_conf()
print(line_conf().__closure__) #(<cell at 0x05BE3530: int object at 0x1DA2D1D0>,
# <cell at 0x05C4DDD0: int object at 0x1DA2D1E0>)
for i in line_conf().__closure__: #打印引用的外部变量值
    print(i.cell_contents) #1  ； #2
#  __closure__属性返回的是一个元组对象，包含了闭包引用的外部变量。
# 若主函数内的闭包不引用外部变量，就不存在闭包，主函数的_closure__属性永远为None：
# 若主函数没有return子函数，就不存在闭包，主函数不存在_closure__属性：


def line_conf3(a):
    b = 1
    def line(x):
        return a * x + b
    return line
line_A = line_conf3(2)
b = 20
print(line_A(1))  # 3
# line_A对象作为line_conf返回的闭包对象，它引用了line_conf下的变量b=1，在print时，全局作用域下定义了新的b变量指向20，最终结果仍然引用的line_conf内的b。这是因为，闭包作为对象被返回时，它的引用变量就已经确定（已经保存在它的__closure__属性中），不会再被修改。是的，闭包在被返回时，它的所有变量就已经固定，形成了一个封闭的对象，这个对象包含了其引用的所有外部、内部变量和表达式。当然，闭包的参数例外。

_list = []
for i in range(3):
    def func3(a):
        return i+a
    _list.append(func3)
for f in _list:
    print(f(1))
# 结果是3, 3, 3 。因为，在Python中，循环体内定义的函数是无法保存循环执行过程中的不停变化的外部变量的，即普通函数无法保存运行环境！

_list = []
for i in range(3):
    def func2(i):
        def f_closure(a):  # <<<---
            return i + a
        return f_closure
    _list.append(func2(i))  # <<<---
for f in _list:
    print(f(1))


_list = []
for i in range(3):
    def func():
        return i+1
    func.__doc__ = i
    func.__hash__ = i
    func.__repr__ = i
    func.__defaults__ = tuple([i]) #这个属性必须是tuple类型
    func.__name__ = f'{i}'
    func.hello = i  #自定义一个属性并赋值
    # 不能再玩了
    _list.append(func)
 
for f in _list:
    print(f.__doc__,
          f.__hash__,
          f.__repr__,
          f.__defaults__,
          f.__name__,
          f.hello,
          f(),
          )
# 输出
# 0 0 0 (0,) 0 0 3
# 1 1 1 (1,) 1 1 3
# 2 2 2 (2,) 2 2 3
# 函数的一些基本属性在定义时就会有一个初始的确定值（不论这个值是由可变或不可变对象构成，都是一个完整拷贝，不受源变量变动影响）； 闭包保存这个变量的原理是一样的，它用的是函数的__closure__属性，这个属性还有一点特殊，它是只读的，不能由人为修改。（function还有一个__code__属性，这个对象很牛）


def who(name):
    def do(what):
        print(name, 'say:', what)
    return do
lucy = who('lucy')
john = who('john')
lucy('i want drink!')
lucy('i want eat !')
lucy('i want play !')
john('i want play basketball')
john('i want to sleep with U,do U?')
lucy("you just like a fool, but i got you!")


import logging
def log_header(logger_name):
    logging.basicConfig(level=logging.DEBUG, format='%(asctime)s [%(name)s] %(levelname)s  %(message)s',
                        datefmt='%Y-%m-%d %H:%M:%S')
    logger = logging.getLogger(logger_name)
 
    def _logging(something,level):
        if level == 'debug':
            logger.debug(something)
        elif level == 'warning':
            logger.warning(something)
        elif level == 'error':
            logger.error(something)
        else:
            raise Exception("I dont know what you want to do?" )
    return _logging
 
project_1_logging = log_header('project_1')
project_2_logging = log_header('project_2')
 
def project_1():
    #do something
    project_1_logging('this is a debug info','debug')
    #do something
    project_1_logging('this is a warning info','warning')
    # do something
    project_1_logging('this is a error info','error')
 
def project_2():
    # do something
    project_2_logging('this is a debug info','debug')
    # do something
    project_2_logging('this is a warning info','warning')
    # do something
    project_2_logging('this is a critical info','error')
 
project_1()
project_2()

# 分组排序
def sort_priority(values, group):
    def helper(x):
        if x in group:
            return(0, x)
        return(1, x)
    values.sort(key = helper)

numbers = [8, 2, 3, 2 ,3, 5, 6, 7]
group = {2, 3, 5, 7}
sort_priority(numbers, group)
print(numbers)  #[2, 2, 3, 3, 5, 7, 6, 8]

def sort_priority2(values, group):
    found = False
    def helper(x):
        if x in group:
            found = True
            return(0, x)
        return(1, x)
    values.sort(key = helper)
    return found

def sort_priority3(values, group):
    found = False
    def helper(x):
        nonlocal found
        if x in group:
            found = True
            return(0, x)
        return(1, x)
    values.sort(key = helper)
    return found

def sort_priority4(values, group):
    found = [False]
    def helper(x):
        if x in group:
            found[0] = True
            return(0, x)
        return(1, x)
    values.sort(key = helper)
    return found