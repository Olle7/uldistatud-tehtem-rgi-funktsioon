a=[float(input("a[TX]b\nsisesta a:")),int(input("(XϵN)sisesta X:")),int(input("(XϵN)sisesta b:"))]
print(str(a[0])+"[T"+str(a[1])+"]"+str(a[2])+"=")
if a[1]==2:
    print(a[0]*a[2])
elif a[1]==1:
    print(a[0]+a[2])
elif a[1]==0:
    print(1)
while len(a)!=1:
    if a[len(a)-1]==1:
        b=a[len(a)-3]
        a=a[:-2]
        a[len(a)-1]=b
    elif a[len(a)-2]==3:
        b=a[len(a)-3],a[len(a)-1]
        a=a[:-2]
        a[len(a)-1]=b[0]**b[1]
    else:
        b=a[len(a)-1],a[len(a)-2],a[len(a)-3]
        a=a[:-3]
        a+=[b[2],b[1]-1,b[2],b[1],b[0]-1]
print(a[0])
