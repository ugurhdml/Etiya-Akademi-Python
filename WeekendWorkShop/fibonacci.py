a = 0
b = 1
toplam = 0

for i in range(20): 
    toplam = a+b
    a = toplam
    b = toplam-b
    print(toplam)