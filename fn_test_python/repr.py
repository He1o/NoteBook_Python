class Student:
    def __init__(self,name):
        self.name = name
    def __repr__(self):
        return ('a student named ' + self.name)
    def __str__(self):
        return ('a sdent named ' + self.name)

b = Student('Kim')
print(repr([1,23]))