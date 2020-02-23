l=[]
sonuc=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]
a=int(input("şifre giriniz:"))
i=1
while(i==1):
    kalan=(a%36)
    l.append(kalan)
    bolum=int(a/36)
    if (bolum>=36):
        i=1
        a=bolum
    else:
        l.append(bolum)
        i=0
    
l.reverse()
print(l)
uzunluk=len(l)
for i in range(uzunluk):
    b=l[i]
    print(sonuc[b],end="")
    