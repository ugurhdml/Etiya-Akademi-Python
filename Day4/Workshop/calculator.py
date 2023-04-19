def toplama ():
    sayi1=int(input("Toplama işlemi için birinci sayıyı giriniz : "))
    sayi2=int(input("Toplama işlemi için ikinci sayıyı giriniz : "))
    print(sayi1,"+",sayi2,"=", sayi1+sayi2)

def cikarma():
    sayi1=int(input("Çıkarma işlemi için birinci sayıyı giriniz : "))
    sayi2=int(input("Çıkarma işlemi için ikinci sayıyı giriniz : "))
    print(sayi1,"-",sayi2,"=", sayi1-sayi2)

def carpma():
    sayi1=int(input("Çarpma işlemi için birinci sayıyı giriniz : "))
    sayi2=int(input("Çarpma işlemi için ikinci sayıyı giriniz : "))
    print(sayi1,"*",sayi2,"=", sayi1*sayi2)

def bolme():
    sayi1=int(input("Bölme işlemi için birinci sayıyı giriniz : "))
    sayi2=int(input("Bölme işlemi için ikinci sayıyı giriniz : "))
    print(sayi1,"/",sayi2,"=", sayi1/sayi2)

def modAlma():
    sayi1=int(input("Mod alma işlemi için birinci sayıyı giriniz : "))
    sayi2=int(input("Mod alma işlemi için ikinci sayıyı giriniz : "))
    print(sayi1,"%",sayi2,"=", sayi1%sayi2)


while True:
    secim=input("Yapmak istediğiniz işlemi giriniz: + --> Toplama  - --> Çıkarma  * --> Çarpma  / --> Bölme  % --> Mod Alma : ")
    
    if secim == "q":
        print("Programdan çıkılıyor...")
        break

    elif secim == '+':
        toplama()
            
    elif secim == '-':
        cikarma()
        
    elif secim == '*':
        carpma()
        
    elif secim == '/':
        bolme()

    elif secim == "%":
        modAlma()

    else:
        print("Geçersiz giriş yaptınız, tekrar deneyiniz...")