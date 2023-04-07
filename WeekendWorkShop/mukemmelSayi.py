sayi = 0
tempSayi =0

while sayi <=1:
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
   

