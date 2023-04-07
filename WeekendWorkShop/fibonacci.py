a = 0
b = 1
c = 0

for i in range(20): 
    c = a+b
    a = c
    b = c-b
    print(c)