import random
from school import School

class Person:
    def __init__(self,name):
        self.name=name

class Teacher(Person):
    def __init__(self, name):
        super().__init__(name)
    def evaluate_exam(self):
        return random.randint(40,100)

class Student(Person):
    def __init__(self, name,classroom):
        super().__init__(name)
        self.__id=None
        self.classroom=classroom #classroom object
        self.marks={} #{'eng':33}
        self.subject_grade={}#{'eng':'F'}
        self.grade=None #starting a kisui thakbe na

    def calculate_final_grade(self):
        sum=0
        for grade in self.subject_grade.values():
            point=School.grade_to_val(grade)
            sum+=point
        gpa=sum/len(self.subject_grade)
        self.grade=School.value_to_grade(gpa)

    @property
    def id(self):
        return self.__id
    
    @id.setter
    def id(self,value):
        self.__id=value
