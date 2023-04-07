sayiListesi = []
enBuyuk = 0
for i in range(10):
    sayi = int(input(f"{i+1}.sayiyi giriniz :"))
    sayiListesi.append(sayi)
   

print(max(sayiListesi))