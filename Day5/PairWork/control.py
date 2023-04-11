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


teacher1 = Teacher("Halit",25)
teacher2 = Teacher("Enes",25)

student1 = Student("Zeynep",28)
student2 = Student("Uğur ",24)
addTeacher(teacher1)
addTeacher(teacher2)

addStudent(student1)
addStudent(student2)
showTeacherList()
showStudentList()







        