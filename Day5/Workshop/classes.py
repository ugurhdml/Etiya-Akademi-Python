from human import Human
# self ---> this
# self ---> sadece bir isimlendirmedir, pythonda class içi fonksiyonlarda parametre zorunludur.
# instance ---> Örnek 
human1 = Human("Uğur")
human1.talk("Merhaba")
human1.walk()
print(human1)


human2 = Human("Enes")
human2.talk("Selam")
human2.walk()
print(human2)