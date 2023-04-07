ustLimit = int(input("Bir üst limit giriniz :"))
secim = int(input("Alt limit belirlemek için 1 tuşlayınız. Belirlemeden devam etmek için 2 tuşlayınız."))

if secim == 1:
    altLimit = int(input("Bir alt limit giriniz :"))
    for i in range(altLimit,ustLimit,2):
        print(i)
elif secim ==2:
    for i in range(0,ustLimit,2):
        print(i)
else:
    print("Geçersiz sayı girdiniz...")
    