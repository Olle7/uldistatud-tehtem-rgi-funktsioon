a=[float(input("a[TX]b\nsisesta a:")),int(input("sisesta naturaalarv X:")),int(input("sisesta naturaalarv b:"))]
print(str(a[0])+"[T"+str(a[1])+"]"+str(a[2])+"=")
if a[1]==2:
    a=[a[0]*a[2]]
elif a[1]==1:
    a=[a[0]+a[2]]
elif a[1]==0:
    a=[1]
while len(a)!=1:
    b=a[len(a)-3],a[len(a)-2],a[len(a)-1]
    a=a[:-3]
    if b[1]==3:
        a.append(b[0]**b[2])
    elif b[2]==1:
        a.append(b[0])
    else:
        a+=[b[0],b[1]-1,b[0],b[1],b[2]-1]
print(a[0])
