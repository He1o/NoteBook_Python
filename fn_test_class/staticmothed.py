class Person(object):

    money = 10

    def __init__(self, name, age):
        self.name = name
        self.age = age
        print('self:', self)  #self: <__main__.Person object at 0x00000259E3CC76D8> 一个类的实例对象

    # 定义一个build方法，返回一个person实例对象，这个方法等价于Person()。
    # @classmethod因为持有cls参数，可以来调用类的属性，类的方法，实例化对象等，避免硬编码
    @classmethod
    def build(cls):
        # cls()等于Person()
        p = cls("Tom", 18)  #cls相当于一个类，self相当于一个实例
        # print('cls:', cls)  #<class '__main__.Person'>  一个类
        return p

    # 不需要传self或者cls参数，与一个单独的函数一样
    # 在@staticmethod中要调用到这个类的一些属性方法，只能直接类名.属性名或类名.方法名。
    @staticmethod
    def construct():
        print(Person.money)

    def destroy(self):
        print('hahh')

    def he(self):
        self.destroy()


if __name__ == '__main__':
    person = Person.build()
    print(person)
    Person.construct()  #如果没有self实例是可以调用的,
    Person.construct()
    Person.heao = 0  #不需要提前定义，可直接赋值
    print(Person.heao)
    # a = Person('heao', 22)
    # a.he()
