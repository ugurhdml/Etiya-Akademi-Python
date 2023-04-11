# class , nesne , obje, sınıf

class Human:
    #property, attribute ---> özellik, nitelik
    name = ""
    age = 20
    
    def __init__(self,name,age) -> None:
        print("Yapıcı blok çalıştı.")
        self.name = name
        self.age = age
        
    
    
    #Davranışlar 
    def talk(self,message):
        print(f"{self.name} : {message}")
        
    def walk(self):
        print(f"{self.name} {self.age} Walking...")
        
        #instance üretmek  - örnek üretmen
        
human1 = Human("Ahmet",25)
human1.name = "Uğur"
human1.age = 24
human1.talk("Merhaba")
human1.walk()
human2 = Human("Ali",16)
human2.walk()
human2.talk("Selamlar")