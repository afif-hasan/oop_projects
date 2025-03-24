class School:
    def __init__(self,name,address):
        self.name=name
        self.address=address
        self.teachers={} #{'subject':teacher_object}
        self.classrooms={} #{'nine':classroom_object}
    def add_classroom(self,classroom):
        self.classrooms[classroom.name]=classroom
    def add_teachers(self,teacher,subject):
        self.teachers[subject.name]=teacher
    def student_admission(self,student):
        student.classroom.add_student(student)

    @staticmethod
    def calculate_grade(marks):
        if marks>=80 and marks<=100:
            return 'A+'
        elif marks>=70 and marks<80:
            return 'A'
        elif marks>=60 and marks<70:
            return 'A-'
        elif marks>=50 and marks<60:
            return 'B'
        elif marks>=40 and marks<50:
            return 'C'
        else:
            return 'F'
        
    @staticmethod
    def grade_to_val(grade):
        grade_mp={
            'A+':5.00,
            'A':4.00,
            'A-':3.50,
            'B':3.00,
            'C':2.50,
            'F':0.00
        }
        return grade_mp[grade]
    
    @staticmethod
    def value_to_grade(value):
        if value>=4.50 and value<=5.00:
            return 'A+'
        elif value>=3.50 and value<4.50:
            return 'A'
        elif value>=3.00 and value<3.50:
            return 'A-'
        elif value>=2.50 and value<3.00:
            return 'B'
        elif value>=2.00 and value<2.50:
            return 'C'
        else:
            return 'F'
    
    def __repr__(self):
        #all classrooom
        print("------Classrooms------")
        for classroom in self.classrooms.keys():
            print(classroom)
        #all teacher
        print("-------Our Teachers-------")
        for key,value in self.teachers.items():
            print(value.name,'-->',key)
        #all student
        for key,value in self.classrooms.items():
            print(f"-----Subjects taught in {value.name}------")
            for subject in value.subjects:
                print(subject.name)
            print(f"----Students of {value.name}------")
            for student in value.students:
                print(student.name)
            print("")        
        #all student's result
        for key,value in self.classrooms.items():
            print(f"-----Result of class {value.name}-------")
            for student in value.students:
                print(f"     ------{student.name}-------")
                for key,value in student.marks.items():
                    print(f"{key} {value} {student.subject_grade[key]}")
                print(f"Semester result: {student.grade}")
            print("")
        return ''