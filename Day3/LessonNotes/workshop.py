biggestValue = 0

#for i in range(10):
    #sayi = int(input(f"{i+1}. Değeri Giriniz : "))
   # if sayi > biggestValue:
    #    biggestValue = sayi
#print(f"Girdiğiniz sayılar arasından en büyük olanı : {biggestValue}")

sayilar = []

for i in range(3):
    sayilar.append(int(input(f"{i+1}. sayıyı giriniz : ")))

sayilar.sort(reverse=True)
enBuyukN = int(input("Sayılar arasından kaçınıcı en büyüğü istiyorsunuz?"))
print(sayilar[enBuyukN-1])
# kullanıcın vereceği üst limit ile
# 0dan üst limite kadar olan tüm çift sayıları yazdıralım
#forRange = int(input("Üst limit belirleyiniz: "))
# for i in range(forRange+1):
#     if i % 2 == 0:
#         print(i)
#start => döngü kaç sayısından başlasından
#stop => döngü kaç sayısında son bulsun
#step => döngü kaç kaç artırılsın
#for i in range(0,forRange+1,2):
    #print(i)
## end


## 3. ister => 2. isterdeki alt limit kullanıcı belirlemelidir
forRangeMin = int(input("Döngünün alt limitini belirleyiniz: "))
forRangeMax = int(input("Döngünün üst limitini belirleyiniz: "))
for i in range(forRangeMin, forRangeMax+1):
    if i % 2 == 0:
        print(i)
##end