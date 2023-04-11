class Teacher:
    name = ""
    age = 0
    department =""
    def __init__(self,name,department,age):
        self.name = name
        self.age = age
        self.department = department
        
    def __repr__(self): 
        return f"İsim: {self.name} Yaş: {self.age} Bölümü: {self.department}" 
        
    