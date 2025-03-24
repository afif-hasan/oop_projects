from school import School
from classroom import Classroom
from subject import Subject
from person import Person,Student,Teacher

shaheen_school=School('Shaheen School','Trishal')

Eight=Classroom('Eight')
Nine=Classroom('Nine')
Ten=Classroom('Ten')

Abul=Teacher('Abul khan')
Kabul=Teacher('Kabul Ahmed')
Mukhles=Teacher('Mukhles Khan')
Habul=Teacher('Habul khan')

Bangla=Subject('Bangla',Mukhles)
English=Subject('English',Habul)
Physics=Subject('Physics',Kabul)
Chemistry=Subject('Chemistry',Abul)
Biology=Subject('Biology',Abul)

Rahim=Student('Rahim',Eight)
Karim=Student('Karim',Eight)
Jamil=Student('Jamil',Eight)

Ashik=Student('Ashik',Nine)
Ratul=Student('Ratul',Nine)
Hamza=Student('Hamza',Nine)

Nobin=Student('Nobin',Ten)
Faruk=Student('Faruk',Ten)
Rasel=Student('Rasel',Ten)

#adding classrooms
shaheen_school.add_classroom(Eight)
shaheen_school.add_classroom(Nine)
shaheen_school.add_classroom(Ten)
#adding teachers
shaheen_school.add_teachers(Abul,Biology)
shaheen_school.add_teachers(Kabul,Physics)
shaheen_school.add_teachers(Mukhles,Bangla)
shaheen_school.add_teachers(Habul,English)
shaheen_school.add_teachers(Abul,Chemistry)
#adding subject to classroom
Eight.add_subject(Bangla)
Eight.add_subject(English)

Nine.add_subject(English)
Nine.add_subject(Physics)
Nine.add_subject(Chemistry)

Ten.add_subject(Physics)
Ten.add_subject(Chemistry)
Ten.add_subject(Biology)

#admitting students
shaheen_school.student_admission(Rahim)
shaheen_school.student_admission(Karim)
shaheen_school.student_admission(Jamil)
shaheen_school.student_admission(Ashik)
shaheen_school.student_admission(Ratul)
shaheen_school.student_admission(Hamza)
shaheen_school.student_admission(Nobin)
shaheen_school.student_admission(Faruk)
shaheen_school.student_admission(Rasel)

Eight.take_semester_final()
Nine.take_semester_final()
Ten.take_semester_final()

print(shaheen_school)

