# 函数也是对象
# 拥有__call__方法的对象都是函数
# Python 中，凡是可以将 () 直接应用到自身并执行，都称为可调用对象。可调用对象包括自定义的函数、Python 内置函数以及本节所讲的类实例对象。

class CLanguage:
    # 定义__call__方法
    def __call__(self,name,add):
        print("调用__call__()方法",name,add)
clangs = CLanguage() 
clangs("heao","aaa") #调用__call__()方法 heao aaa

# 该方法的功能类似于在类中重载 () 运算符，使得类实例对象可以像调用普通函数那样，以“对象名()”的形式使用。
#对于可调用对象，实际上“名称()”可以理解为是“名称.__call__()”的简写。仍以上面程序中定义的 clangs 实例对象为例，其最后一行代码还可以改写为如下形式：
clangs.__call__("heao","aaa")  #调用__call__()方法 heao aaa

def say():
    print("aaaaa")
say()  #
say.__call__()  #函数也是对象


# 用 __call__() 弥补 hasattr() 函数的短板
class CLanguage2:
    def __init__ (self):
        self.name = "heao"
        self.add = "lalalall"
    def say(self):
        print("hhhhhhh")
clangs = CLanguage2()
if hasattr(clangs,"name"):
    print(hasattr(clangs.name,"__call__"))
print("**********")
if hasattr(clangs,"say"):
    print(hasattr(clangs.say,"__call__"))

# False
# **********
# True

# hasattr() 函数的用法，该函数的功能是查找类的实例对象中是否包含指定名称的属性或者方法，但该函数有一个缺陷，即它无法判断该指定的名称，到底是类属性还是类方法。
# 要解决这个问题，我们可以借助可调用对象的概念。要知道，类实例对象包含的方法，其实也属于可调用对象，但类属性却不是。
# 可以看到，由于 name 是类属性，它没有以 __call__ 为名的 __call__() 方法；而 say 是类方法，它是可调用对象，因此它有 __call__() 方法。