l=[]
m=[]
z=[]
v=[]
sonuc=["A","B","C","D","E","F","G","H","I","J","K","L","M","N","O","P","Q","R","S","T","U","V","W","X","Y","Z",
       "a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z",
       "0","1","2","3","4","5","6","7","8","9","+","/","="]

l=input("kelime gir:")
a=len(l)
ak=(a*8)
mod=(ak%24)
if ((mod)==0):
    aktif=1
    eks=int(ak/6)
    ekle=0
    ek=0
else:
    aktif=0
    ek=(24-mod)
    eks=0
    ekle=int(((ak+ek)/6))
#print(mod,"-")
#print(ek)
#print(eks,"*")
for i in range(a):
    k=(ord(l[i]))
#    print(k,"/")
    kaktif=0
    if (k<=63):
        kaktif=1
    else:
        pass
    #r=1
    while True:
        w=k%2
        m.append(w)
        k=int(k/2)
        if(k==1):
            m.append(k)
            if (kaktif==1):
                m.append(0)
                kaktif=0
            else:
                pass
            m.reverse()
            break
#    print(m,"*")
    p=len(m) 
    print(p)
    for i in range(p):
        z.append(m[i])
#    print(z,"/")
    m.clear()  
b=0
for i in range(a):
    if b==(8*i):
        z.insert(b,0)
        b=b+8
    else:
        pass
#print(z,"+")    
for i in range(ek):
    if aktif==1:
        break
    else:
        z.append(0)
#print(z)        
for i in range(eks+ekle):
    for j in range(6):
        m.append(z[j])
#    print(m,"--")
    m.reverse()
    h=0        
    for j in range(6):
        u=m[j]
        d=(u*(2**j))
        if(d!=0):
            h=h+d
        else:
            kal=64
    if (h!=0):
        v.append(h)
    else:
        v.append(kal)
    m.clear()
    for i in range(6):
        z.pop(0)
#print(v)
deger=len(v)
for i in range(deger):
    c=v[i]
    print(sonuc[c],end="")




