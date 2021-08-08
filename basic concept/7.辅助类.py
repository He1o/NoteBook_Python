import collections
Grade = collections.namedtuple('Grade', ('score', 'weight'))

class Subject(object):
    def __init__(self, name):
        self._name = name
        self._grades = []

    def report_grade(self,  score, weight):
        self._grades.append(Grade(score, weight))

    def average_grade(self):
        total, total_weight = 0, 0
        for grade in self._grades:
            total += grade.score * grade.weight
            total_weight += grade.weight
        return total / total_weight

class Student(object):
    def __init__(self):
        self._subjects = {}

    def report_grade(self, sub, score, weight):
        if not sub in self._subjects:
            self._subjects[sub] = Subject(sub)
        self._subjects[sub].report_grade(score, weight)
        return self._subjects[sub]

    def average_grade(self):
        total, count = 0, 0
        for item, subject in self._subjects.items():
            total += subject.average_grade()
            count += 1
        return total / count

class Book(object):
    def __init__(self):
        self._students = {}

    def student(self, name):
        if name not in self._students:
            self._students[name] = Student()
        return self._students[name]

book = Book()
heao = book.student('heao')
heao.report_grade('math', 90, 0.5)
heao.report_grade('math', 40, 0.5)
heao.report_grade('chiness', 100, 0.5)
heao.report_grade('chiness', 100, 0.5)
print(heao.average_grade())