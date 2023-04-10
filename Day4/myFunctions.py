def mukemmelSayiHesapla():
    tempSayi=0
    sayi=0
    while sayi <1:
        sayi = int(input("Bir sayı giriniz : "))
        if sayi < 1: 
            print("Geçersiz Sayı girdiniz. Tekrar giriş yapınız.")
        else:
            for i in range(1,sayi):
                if sayi % i == 0:  
                    tempSayi+=i

    if tempSayi==sayi:
        print("Girdiğiniz sayi mükemmel sayidir.")
    else:
        print("Girdiğiniz sayı mükemmel sayı değildir.")

mukemmelSayiHesapla()
#-------------------------------------------------------------------
def fibonacci():
    a = 0
    b = 1
    toplam = 0

    for i in range(20): 
        toplam = a+b
        a = toplam
        b = toplam-b
        print(toplam)

fibonacci()

#-------------------------------------------------------------------

def ciftSayilar():
    ustLimit = int(input("Bir üst limit giriniz :"))
    secim = int(input("Alt limit belirlemek için 1 tuşlayınız. Belirlemeden devam etmek için 2 tuşlayınız."))

    if secim == 1:
        altLimit = int(input("Bir alt limit giriniz :"))
        for i in range(altLimit,ustLimit):
            if i % 2 ==0:
                print(i)
    elif secim ==2:
        for i in range(0,ustLimit,2):
            print(i)
    else:
        print("Geçersiz sayı girdiniz...")

ciftSayilar()

#-------------------------------------------------------------------

def sayiSiralama():
    sayiListesi = []

    for i in range(10):
        sayi = int(input(f"{i+1}.sayiyi giriniz :"))
        sayiListesi.append(sayi)
        print(max(sayiListesi))
        
sayiSiralama()
