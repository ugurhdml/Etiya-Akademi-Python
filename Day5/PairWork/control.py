from student import Student
from teacher import Teacher

teacherList = []
studentList = []

def addStudent(student):
        studentList.append(student)

def addTeacher(teacher):
        teacherList.append(teacher)

def showTeacherList():
    print(f"Öğretmenler : {teacherList}")
    
def showStudentList():
    print(f"Öğrenciler  : {studentList}")


teacher1 = Teacher("Halit","Python",25)
teacher2 = Teacher("Engin","Java",37)

student1 = Student("Zeynep",28,674)
student2 = Student("Uğur ",24,1070)
addTeacher(teacher1)
addTeacher(teacher2)

addStudent(student1)
addStudent(student2)
showTeacherList()
showStudentList()







        