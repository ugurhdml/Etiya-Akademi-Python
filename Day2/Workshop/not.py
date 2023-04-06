vize=float(input("Vize notunuzu giriniz: "))
final=float(input("Final notunuzu giriniz: "))
ortalama =(vize*0.4)+(final *0.6)

if ortalama <= 49 and ortalama >=0 :
   print("Ortalama: ", ortalama)
   print("Harf notu: FF")
elif ortalama <= 59 :
   print("Ortalama: ", ortalama)
   print("Harf notu: DD")
elif ortalama <= 69 :
   print("Ortalama: ", ortalama)
   print("Harf notu: CC")
elif ortalama <= 79 :
   print("Ortalama: ", ortalama)
   print("Harf notu: BB")
elif ortalama <= 100 :
   print("Ortalama: ", ortalama)
   print("Harf notu: AA")
else:
   print("Geçersiz Giriş")
