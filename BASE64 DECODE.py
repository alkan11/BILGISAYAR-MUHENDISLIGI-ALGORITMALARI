l=[]
m=[]
v=[]
z=[]
c=[]
sonuc=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
       "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
       "0","1","2","3","4","5","6","7","8","9","+","/","="]

l=input("şifre gir:")
a=len(l)
s=0
for i in range(a):
    for j in range(64):
        if l[i]==sonuc[j]:
            index=sonuc.index(sonuc[j])
            break
        else:
            continue 
    bolum=0
    if (index<=31):
        dongu=5
        if (index<=15):
            dongu=4
            if (index<=7):
                dongu=3
                if (index<=3):
                    dongu=2
                    if (index<=1):
                        dongu=1
                    else:
                        print("hata var")
                else:
                    pass
            else:
                pass
        else:
            pass
    else:
        dongu=6
        
        
    print(dongu)       
    for i in range(dongu):
        mod=index%2
        index=int(index/2)
        m.append(mod)
    m.reverse()
    kontrol=(6-dongu)
    for i in range(kontrol):
        m.insert(i,0)
    for i in range(6):
        v.append(m[i])
    m.clear()    

#print(v)
dongutwo=(len(v))
#print(dongutwo)
bolum=int(dongutwo/8)
for i in range(bolum):
    for j in range(8):
        z.append(v[j])
    z.reverse()
    toplam=0
    for i in range(8):
        deger=z[i]
        if (deger!=0):
            carpım=(deger*(2**i))
            toplam=toplam+carpım
        else:
            continue
    c.append(toplam)
    
    for j in range(8):
        v.pop(0)
        z.pop(0)
print("base10-->",end="")
print(c) 
print("base10(metin)-->",end="")
for i in range(len(c)):
    print(chr(c[i]),end="")

   











#print(m)        