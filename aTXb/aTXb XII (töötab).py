a=[float(input("a[TX]b\nsisesta a:")),int(input("sisesta X:")),int(input("sisesta b:"))]
print(str(a[0])+"[T"+str(a[1])+"]"+str(a[2])+"=")
if a[1]==2:
    a=[a[0]*a[2]]
elif a[1]==1:
    a=[a[0]+a[2]]
elif a[0]==int(a[0]):
    a[0]=int(a[0])
elif a[1]==0:
    a=[1]
while len(a)!=1:
    if a[len(a)-1]==1:
        a=a[:-3]+[a[len(a)-3]]
    elif a[len(a)-2]==3:#peax if a[len(a)-1]==1:´ga vahetuses olema?
        try:
            a=a[:-3]+[a[len(a)-3]**a[len(a)-1]]
        except OverflowError:
            a=a[:-2]+[3,a[len(a)-1]]
            break
    elif 1500>a[len(a)-1]:#kas saab selle kirjutada while tingimuseks
        a=a[:-2]+[a[len(a)-2]-1,a[len(a)-3]]*int(a[len(a)-1]-1)
    else:
        break
b=str(a[0])
for c in range(1,len(a)-1,2):
    b+="[T"+str(a[c])+"]("+str(a[c+1])
print(b+")"*(len(a)//2))
