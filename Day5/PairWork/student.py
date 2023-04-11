#Bir okul kayıt sistemi kodlayalım;

#Öğrenci ve Öğretmen classlarını farklı dosyalarda oluşturalım. Bu classlar içerisinde en az 2 property 2 method barındırmalıdır.
#Daha sonra bir dosyada öğrenci ve öğretmen classlarını import ederek bir listede kayıtlı öğrenci/öğretmen bilgilerini ayrı ayrı tutalım.
#Listeye ekleme yapan, listedeki tüm elemanları ekrana yazan fonksiyonları geliştirelim ve konsolda test edelim.
#Classlarımız içerisinde self keywordü kullanalım. Class içi fonksiyonlarda içerideki propertylerden yararlanalım.

class Student:
    name = ""
    age = 0
    def __init__(self,name,age):
        self.name = name
        self.age = age
        
    def __repr__(self): 
        return f"{self.name} {self.age}" 
        
    
    
    
        
                
    

    

        
    


        
