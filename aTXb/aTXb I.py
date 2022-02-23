def leia_sulgude_siseseim_avaldis(avaldis):
    s=0
    s_max=0
    Sid=[]
    sulgude_siseseim_avaldis=""
    for mark in(list(avaldis)):
        if mark =="(":#kui vaadeldav tähemärk on "(",siis sulgude sisesus +=1
            s+=1
        elif mark ==")":#kui vaadeldav tähemärk on "(",siis sulgude sisesus +=-1
            s+=-1
        print(s,mark)
        Sid.append(s)#lisa kõikide märkide sulgude sisesus arv hulka Sid
    print(max(Sid),"\ns",sulgude_siseseim_avaldis)
    I=Sid.index(max(Sid))
    II=Sid.index(max(Sid))+Sid.count(max(Sid))
    print(str(I)+" kuni "+str(II))
    for indeks in range(I+1,II,1):
        print(indeks)
        print(list(avaldis)[indeks])
        sulgude_siseseim_avaldis+=list(avaldis)[indeks]
        print(sulgude_siseseim_avaldis)

leia_sulgude_siseseim_avaldis("(ytf((h(a(s+m))(s)(d)ff)g))")
print("a[TX]b")
X=input("sisesta X: ")
a=input("sisesta a: ")
b=input("sisesta b: ")
avaldis=("("+str(a)+"[T"+str(X)+"]"+str(b)+")=")#teeb andmed avaldiseks
print(avaldis)
