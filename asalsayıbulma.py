a = int(input("bir sayı giriniz  : "))
asayilar = []
bln = []

i = 2

while i<=a:
    k = 1
    while k<=i:
        if i%k==0:
            bln.append(k)
               
        k = k+1
    if len(bln)==2:
        asayilar.append(i)
    bln.clear()
    i=i+1
print(asayilar)

