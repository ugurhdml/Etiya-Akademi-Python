from student import Student
from teacher import Teacher

teacherList = []
studentList = []


def addStudent(student):
        studentList.append(student)

def addTeacher(teacher):
        teacherList.append(teacher)

def showTeacherList():
    for teacher in teacherList:
        print(teacher.name," ",teacher.department," ",teacher.age)
        
    
def showStudentList():  
    for student in studentList:
        print(student.name," ",student.age," ",student.number)
    

# teacher1 = Teacher("Halit","Python",25)
# teacher2 = Teacher("Engin","Java",37)
# student1 = Student("Zeynep",28,674)
# student2 = Student("Uğur ",24,1070)
# addTeacher(teacher1)
# addTeacher(teacher2)
# addStudent(student1)
# addStudent(student2)
# showTeacherList()
# showStudentList()

while True:
    print("Güncel öğretmen ve öğrenci listesini görüntülemektesiniz.")
    showTeacherList()
    showStudentList()
    secim = input("Öğrenci eklemek için 1 , Öğretmen eklemek için 2, çıkmak için q tuşlayınız:")
    if secim == "1":
        isim = input("isim giriniz :")
        yas = int(input("yas giriniz :"))
        numara = int(input("numara giriniz :"))
        student = Student(isim,yas,numara)
        addStudent(student)
    elif secim =="2":
        isim = input("isim giriniz :")
        depart = input("Departman giriniz :")
        yas = int(input("Yaş giriniz :"))
        teacher = Teacher(isim,depart,yas)
        addTeacher(teacher)
    elif secim =="q":
        print("Hoşçakalın.")
        break
    else:
        print("Hatalı giriş yaptınız tekrar deneyiniz.")
        
        
        
            
        
            







    