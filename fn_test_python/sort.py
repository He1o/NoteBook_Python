list1 = [2, 4, 5, 2, 8, 5]
b = list1.sort()  # None 直接改变list1的内容，返回值为None
print(list1)  #[2, 2, 4, 5, 5, 8]

# sorted 不直接改变原来迭代对象
sorted([5, 2, 3, 1, 4])  #[1, 2, 3, 4, 5]
# list.sort()方法只能用于列表，相对的，sorted()函数则适用于所有的可迭代对象
sorted({1: 'D', 2: 'B', 3: 'B', 4: 'E', 5: 'A'})  #[1, 2, 3, 4, 5]

sorted("This is a test string from Andrew".split(), key=str.lower)
# ['a', 'Andrew', 'from', 'is', 'string', 'test', 'This']   
# 字符串大小不敏感

# key参数对应的值，必须是这样一个函数：接受一个参数然后返回一个用来排序的键。用这种技术来排序在速度上是非常快的，因为key函数恰好被每一个输入记录调用一次。一种常用的模式是，在对复杂对象进行排序的时候，使用这个对象的索引作为排序的键，例如：

student_tuples = [
    ('john', 'A', 15),
    ('jane', 'B', 12),
    ('dave', 'B', 10),
    ]
sorted(student_tuples, key=lambda student: student[2])   # sort by age
# [('dave', 'B', 10), ('jane', 'B', 12), ('john', 'A', 15)]

class Student:
    def __init__(self, name, grade, age):
        self.name = name
        self.grade = grade
        self.age = age
    def __repr__(self):
        return repr((self.name, self.grade, self.age))

student_objects = [
    Student('john', 'A', 15),
    Student('jane', 'B', 12),
    Student('dave', 'B', 10),
]
sorted(student_objects, key=lambda student: student.age)   # sort by age
# print(student_objects) [('john', 'A', 15), ('jane', 'B', 12), ('dave', 'B', 10)]


a = 'wwfsldjfe'
print(b)