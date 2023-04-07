# Diziler Listeler start
sayilar = [100,200,300,400,500, "merhaba", 15.5, True] # Liste elemanlarının veri tipleri aynı olmak zorunda değil!!!!

#index 0 dan başlar!!  son eleman -1 ile çağrılabilir.
print(sayilar[0])
print(sayilar[5])

print(sayilar)
sayilar.append(600) # --> listenin sonuna eleman ekler!
print(sayilar)
sayilar.pop() # ---> Eğer index verilmez ise en sondaki eleman silinir.

print(sayilar)
sayilar.remove(200) # ---> indexe göre değil değere göre siler. Yalnızca ilk bulunan değer silinir.
sayilar.extend([700,800,900]) # ---> tek bir değer değil listedeki tüm elemanları listeye ekler.

sayilar.clear()
print(sayilar)

# Diziler Listeler end

#String interpolation -start
hello = "Merhaba"
userName = "Uğur"
totalText = hello + " " + userName
print(hello+userName)

totalText = "{message} Sayın {name}".format(message=hello, name=userName)
print(totalText)

#f-string
totalText = f"Merhaba {userName}"
print(totalText)


#String interpolation -end

#karar yapıları start
#ortalamaNot = input("Lütfen ortalamanızı giriniz : ")

# numerik ---> int , double
    #type conversion start
#ortalamaNotAsInteger =int(ortalamaNot)
    #type conversion end
# if else blokları

#indent 
#if ortalamaNotAsInteger > 80:
 #   print("Bravo")
   # print("Tebrikler, Geçtiniz!!!")
#elif ortalamaNotAsInteger > 60:
  #  print("ortalama")
#elif ortalamaNotAsInteger > 50:
 #   print("Normal")
#else:
#    print("Üzgünüm, Kaldınız :( ") 


vize = float(input("Vize notunuzu giriniz : "))
final = float(input("Final notunuzu giriniz : "))
ortalama = (vize* 0.6) + (final * 0.4)

#eğer final 40 dan küçükse kullanıcı kaldı.
#eğer ortalama 50'den küçükse kullanıcı kaldı.
#eğer vize finalin 2 katı ise kullanıcı kaldı.


if final < 40:
    print("Kaldınız !")
elif ortalama < 50:
    print("Kaldınız !")
elif vize >= final * 2:
    print("Kaldınız ! ")
else:
    print("Tebrikler geçtiniz !")

#karar yapıları end
