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