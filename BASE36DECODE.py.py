g=[]
c=[]
sonuc=["0","1","2","3","4","5","6","7","8","9","A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

a=input("karakter giriniz:")
g=(a.upper())
print(g)
uzunluk=len(g)
for i in range(uzunluk):
    for j in range(35):
        if sonuc[j]==g[i]:
            c.append(j)
            break
        else:
            pass
print(c)
uzunlukt=len(c)
for i in range(uzunlukt):
    if i<=1:
        if i==0:
           toplam=(c[i]*36)
        else:
           toplam+=c[i] 
    else:
        toplam=(toplam*36)+(c[i])
print(toplam)