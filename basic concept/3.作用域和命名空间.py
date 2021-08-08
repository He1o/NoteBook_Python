'''命名空间'''
#A namespace is a mapping from names to objects.Most namespaces are currently implemented as Python dictionaries。
# 命名空间(Namespace)是从名称到对象的映射，大部分的命名空间都是通过 Python 字典来实现的。
# 命名空间提供了在项目中避免名字冲突的一种方法。各个命名空间是独立的，没有任何关系的，所以一个命名空间中不能有重名，但不同的命名空间是可以重名而没有任何影响。
# 一般有三种命名空间：
# 内置名称（built-in names）， Python 语言内置的名称，比如函数名 abs、char 和异常名称 BaseException、Exception 等等。
# 全局名称（global names），模块中定义的名称，记录了模块的变量，包括函数、类、其它导入的模块、模块级的变量和常量。
# 局部名称（local names），函数中定义的名称，记录了函数的变量，包括函数的参数和局部定义的变量。（类中定义的也是）

# 命名空间查找顺序:
# 假设我们要使用变量 runoob，则 Python 的查找顺序为：局部的命名空间去 -> 全局命名空间 -> 内置命名空间。
# 如果找不到变量 runoob，它将放弃查找并引发一个 NameError 异常:

# 命名空间的生命周期：
# 命名空间的生命周期取决于对象的作用域，如果对象执行完成，则该命名空间的生命周期就结束。
# 因此，我们无法从外部命名空间访问内部命名空间的对象。

'''作用域'''
# A scope is a textual region of a Python program where a namespace is directly accessible. "Directly accessible" here means that an unqualified reference to a name attempts to find the name in the namespace.
# 作用域就是一个 Python 程序可以直接访问命名空间的正文区域。
# 在一个python程序中，直接访问一个变量，会从内到外依次访问所有的作用域直到找到，否则会报未定义的错误。
# Python 中，程序的变量并不是在哪个位置都可以访问的，访问权限决定于这个变量是在哪里赋值的。
# 变量的作用域决定了在哪一部分程序可以访问哪个特定的变量名称。Python的作用域一共有4种，分别是：
# L（Local）：最内层，包含局部变量，比如一个函数/方法内部。
# E（Enclosing）：包含了非局部(non-local)也非全局(non-global)的变量。比如两个嵌套函数，一个函数（或类） A 里面又包含了一个函数 B ，那么对于 B 中的名称来说 A 中的作用域就为 nonlocal。
# G（Global）：当前脚本的最外层，比如当前模块的全局变量。
# B（Built-in）： 包含了内建的变量/关键字等。最后被搜索
# 规则顺序： L –> E –> G –>gt; B。
# 在局部找不到，便会去局部外的局部找（例如闭包），再找不到就会去全局找，再者去内置中找。
'''
g_count = 0  # 全局作用域
def outer():
    o_count = 1  # 闭包函数外的函数中
    def inner():
        i_count = 2  # 局部作用域
'''


# 内置作用域
# import builtins
# print(dir(builtins))
# 'ArithmeticError', 'AssertionError', 'AttributeError', 'BaseException', 'BlockingIOError', 'BrokenPipeError', 'BufferError', 'BytesWarning', 'ChildProcessError', 'ConnectionAbortedError', 'ConnectionError', 'ConnectionRefusedError', 'ConnectionResetError', 'DeprecationWarning', 'EOFError', 'Ellipsis', 'EnvironmentError', 'Exception', 'False', 'FileExistsError', 'FileNotFoundError', 'FloatingPointError', 'FutureWarning', 'GeneratorExit', 'IOError', 'ImportError', 'ImportWarning', 'IndentationError', 'IndexError', 'InterruptedError', 'IsADirectoryError', 'KeyError', 'KeyboardInterrupt', 'LookupError', 'MemoryError', 'ModuleNotFoundError', 'NameError', 'None', 'NotADirectoryError', 'NotImplemented', 'NotImplementedError', 'OSError', 'OverflowError', 'PendingDeprecationWarning', 'PermissionError', 'ProcessLookupError', 'RecursionError', 'ReferenceError', 'ResourceWarning', 'RuntimeError', 'RuntimeWarning', 'StopAsyncIteration', 'StopIteration', 'SyntaxError', 'SyntaxWarning', 'SystemError', 'SystemExit', 'TabError', 'TimeoutError', 'True', 'TypeError', 'UnboundLocalError', 'UnicodeDecodeError', 'UnicodeEncodeError', 'UnicodeError', 'UnicodeTranslateError', 'UnicodeWarning', 'UserWarning', 'ValueError', 'Warning', 'WindowsError', 'ZeroDivisionError', '__build_class__', '__debug__', '__doc__', '__import__', '__loader__', '__name__', '__package__', '__spec__', 'abs', 'all', 'any', 'ascii', 'bin', 'bool', 'breakpoint', 'bytearray', 'bytes', 'callable', 'chr', 'classmethod', 'compile', 'complex', 'copyright', 'credits', 'delattr', 'dict', 'dir', 'divmod', 'enumerate', 'eval', 'exec', 'exit', 'filter', 'float', 'format', 'frozenset', 'getattr', 'globals', 'hasattr', 'hash', 'help', 'hex', 'id', 'input', 'int', 'isinstance', 'issubclass', 'iter', 'len', 'license', 'list', 'locals', 'map', 'max', 'memoryview', 'min', 'next', 'object', 'oct', 'open', 'ord', 'pow', 'print', 'property', 'quit', 'range', 'repr', 'reversed', 'round', 'set', 'setattr', 'slice', 'sorted', 'staticmethod', 'str', 'sum', 'super', 'tuple', 'type', 'vars', 'zip'

# python 中只有模块（module），类（class）以及函数（def、lambda）才会引入新的作用域，其它的代码块（如 if/elif/else/、try/except、for/while等）是不会引入新的作用域的，也就是说这些语句内定义的变量，外部也可以访问，如下代码：
# if True:
#     msg = 'I am from Runoob'
# print(msg)  #I am from Runoob


# 全局变量和局部变量
# 定义在函数内部的变量拥有一个局部作用域，定义在函数外的拥有全局作用域。
# 局部变量只能在其被声明的函数内部访问，而全局变量可以在整个程序范围内访问。调用函数时，所有在函数内声明的变量名称都将被加入到作用域中。如下实例：

total = 0 # 这是一个全局变量
# 可写函数说明
def sum( arg1, arg2 ):
    #返回2个参数的和."
    total = arg1 + arg2 # total在这里是局部变量.
    # print ("函数内是局部变量 : ", total)  #函数内是局部变量 :  30
    return total
 
#调用sum函数
sum( 10, 20 )
# print ("函数外是全局变量 : ", total)  #函数外是全局变量 :  0

# global
# global不是声明变量，在变量赋值之前，变量是一定不存在的，就算是被global修饰了也一样不存在，所以下面的代码是错的。实际上，global有点类似于声明变量的名称空间，而非变量。
num = 1
def fun1():
    global num  # 需要使用 global 关键字声明
    # print(num)  # 1
    num = 123
    # print(num)  #123
fun1()
# print(num)  #123


# nonlocal
def outer():
    num = 10
    def inner():
        nonlocal num   # nonlocal关键字声明
        num = 100
        # print(num)  #100
    inner()
    # print(num)  #100
outer()

x=3
def g():
    print(x) # 引用全局变量x

def f1():
    # x += 3  #函数内部只要是赋值操作就表示声明为本地变量。UnboundLocalError: local variable 'x' referenced before assignment
    print(x)
f1()

# 全局变量
# 每个py文件(模块)都有一个自己的全局范围
# 文件内部顶层的，不在def区块内部的变量，都是全局变量
# def内部声明(赋值)的变量默认是本地变量，要想让其变成全局变量，需要使用global关键字声明
# def内部如果没有声明(赋值)某变量，则引用的这个变量是全局变量

# 通过import可以导入其他模块的全局变量
# 也可以在当前模块文件中使用import mod_name导入当前模块，其中mod_name为当前文件名，这样就可以在函数内部直接访问全局变量，而无需使用global关键字。
x=3
 
def f():
 global x
 x += 2
 
def f1():
 x=4 # 本地变量
 
def f2():
 x=4 # 本地变量
 import b
 b.x += 2 # 全局变量
 
def f3():
 x=4 # 本地变量
 import sys
 glob = sys.modules['b']
 glob.x += 2 # 全局变量
 
def test():
 print("aaa",x) # 输出3
 f();f1();f2();f3()
 print("bbb",x) # 输出9