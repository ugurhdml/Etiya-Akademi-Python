class Teacher:
    name = ""
    age = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __repr__(self): 
        return f"{self.name} {self.age}" 
        
    