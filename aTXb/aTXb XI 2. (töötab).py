a=[float(input("a[TX]b\nsisesta a:")),int(input("(XϵN)sisesta X:")),int(input("(bϵN)sisesta b:"))]
print(str(a[0])+"[T"+str(a[1])+"]"+str(a[2])+"=")
if a[1]==2:
    a=[a[0]*a[2]]
elif a[1]==1:
    a=[a[0]+a[2]]
elif a[1]==0:
    a=[1]
while len(a)!=1:
    if a[len(a)-1]==1:
        b=a[len(a)-3]
        a=a[:-3]+[b]
    elif a[len(a)-2]==3:#peax if a[len(a)-1]==1:´ga vahetuses olema?
        b=a[len(a)-3],a[len(a)-1]
        try:
            a=a[:-3]+[b[0]**b[1]]
            a[len(a)-1]=b[0]**b[1]#ühendatud
        except OverflowError:
            a=(a[:-3]+[b[0],3,b[1]])#ühendatud
            b=str(a[0])
            for c in range(1,len(a)-1,2):
                b+=("[T"+str(a[c])+"]("+str(a[c+1]))
            print(b+")"*(len(a)//2))
            quit("Arv on liiga suur ,et edasi arvutada.")
    else:
        b=a[len(a)-1],a[len(a)-2],a[len(a)-3]#Kui b on suur peax neid mingi arv kordusi lisama?Sellest ka näilised kinni jooksmised.
        a=a[:-3]+[b[2],b[1]-1,b[2],b[1],b[0]-1]
print(a[0])
