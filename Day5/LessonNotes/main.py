# Fonksiyonlar  start
# definition

def ortalamaHesapla():
    final = 60
    vize = 100
    ortalama = (vize*0.4) + (final*0.6)
    print(ortalama)
    
def ortalamaHesaplaVeDondur(vize,final):
    #expression
    return (vize*0.4) + (final*0.6)
    
#Triggerlamak, çalıştırmak, execute etmek, methodu çağırmak, fonksiyonu çağırmak.

ortalamaHesapla()
benimOrtalamam2 = ortalamaHesapla()

print(benimOrtalamam2)
print(ortalamaHesaplaVeDondur(5,10))
# Fonksiyonlar end
