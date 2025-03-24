from school import School

class Classroom:
    def __init__(self,name):
        self.name=name
        self.students=[]
        self.subjects=[]
    def add_student(self,student):
        roll_no=f"{self.name}-{len(self.students)+1}"#six-1
        student.id=roll_no
        self.students.append(student)#student object
    def add_subject(self,subject):
        self.subjects.append(subject)#subject object
    def take_semester_final(self):
        for subject in self.subjects:
            subject.exam(self.students)
        for student in self.students:
            student.calculate_final_grade()
        
