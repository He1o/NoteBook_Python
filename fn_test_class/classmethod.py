# 当使用某个类的方法时，要先实例化一个对象再调用方法
# @classmethod不需要self参数，但第一个参数需要是表示自身类的cls参数。
# self指向自身实例的一个变量，解释器会自动传递
# 仅仅与类交互而不是和实例交互的方法就是classmethod
HEAO = 0
class Dog(object):

    num = 0
    def __init__(self):
        Dog.num += 1
        self.n = 0

    @classmethod
    def how_many(cls):
        print(cls.num)

a = Dog()
b = Dog()
# print(a.num)  
Dog.how_many() #想统计Dog创建了几个实例，只与类有关与单个实例无关。  # 2

