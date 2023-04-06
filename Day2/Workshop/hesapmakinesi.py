sayi1=int(input("Birinci sayıyı giriniz: "))
sayi2=int(input("İkinci sayıyı giriniz: "))
secim=input("Yapmak istediğiniz işlemi giriniz: + = Toplama  - = Çıkarma  * = Çarpma  / = Bölme : ")

if secim == '+':
   print(sayi1,"+",sayi2,"=", sayi1+sayi2)
 
elif secim == '-':
   print(sayi1,"-",sayi2,"=", sayi1-sayi2)
 
elif secim == '*':
   print(sayi1,"*",sayi2,"=", sayi1*sayi2)
 
elif secim == '/':
   print(sayi1,"/",sayi2,"=", sayi1/sayi2)
else:
   print("Geçersiz Giriş")