# classes.py içindeki Human'ı kullan.
# import classes --> tüm classes modülünü import eder.
from classes import Human #--> classes modülünden Human'ı import eder.
import random
import openpyxl
# --> pythondaki hazır modüller.
#Alias 

#from classes import Human as Insan
#import classes as Classlarım


human3 = Human("Serkan", 19)
human3.talk("Selam")

print(random.randint(1,100))
