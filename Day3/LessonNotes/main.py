# Döngüler start
for i in range (0,10):
    print(i)

ogrenciler = ["Volkan" ,"Ahmet","Sevgi","Derin","Uğur"]


#Break ---> Döngünün kırılacağı noktayı belirlemek için kullanılır.
for i in range(len(ogrenciler)):
    if i ==3:
        break
    print(f"{i+1}. Öğrenci {ogrenciler[i]}")

#Pass  ---> İlgili alanın bodysini boş bırakabilmemizi sağlar.
for i in range(0,10):
    pass    

for ogrenci in ogrenciler:
    if ogrenci =="Uğur":
        continue
    print(f"Ogrenci : {ogrenci}")

#While Start
i = 0
while i < 10:
    i+=1
    if i ==3:
        break
    print(f"While içerisindeki i değeri : {i}")

#While End
# Döngüler End

