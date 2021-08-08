class DOG(object):
    def __init__(self):
        print('in DoG')
        self.name = "jinmao"
        # print(self.name)
        print('out DoG')

class myDOG(DOG):
    def __init__(self):
        print('in myDoG')
        super().__init__()  #第一种可以略过super括号内容
        self.name = "wodejinmao"
        # print(self.name)
        print('out myDoG')

class herDOG(DOG):
    def __init__(self):
        print('in herDoG')
        super(herDOG,self).__init__() #第二种__class__,第一个arg
        self.name = "tadejinmao"
        # print(self.name)
        print('out herDoG')

class hisDOG(DOG):
    def __init__(self):
        print('in hhisDoG')
        # super(herDOG,self).__init__() #第二种__class__,第一个arg
        DOG.__init__(self)
        # self.name = "tadehashiqi"
        # print(self.name)
        print('out hisDoG')

class ourDOG(myDOG,herDOG):
    def __init__(self):
        print('in ourDoG')
        super().__init__()
        print('in ourDoG')

o = ourDOG().name  #继承第一个class的名字
print(o)