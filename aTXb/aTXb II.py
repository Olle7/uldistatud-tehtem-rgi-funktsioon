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
        Sid.append(s)#lisa kõikide märkide sulgude sisesus arv hulka Sid
    for indeks in range(Sid.index(max(Sid))+1,Sid.index(max(Sid))+Sid.count(max(Sid)),1):#maksimaalseste sulusisesustega tähtede indeksid
        sulgude_siseseim_avaldis+=list(avaldis)[indeks]#vastava indeksiga täht liida avaldisse
    return(sulgude_siseseim_avaldis)
def leia_avaldisest_a_b_X(avaldis):
    print(avaldis)
    k=0
    a=""
    b=""
    X=""
    for mark in(list(avaldis)):
        if mark.isdigit() is False and mark != "." :
            print("k+1")
            k+=1
        elif k==0:
            a+=mark
            print("a+",str(mark))
        elif k==2:
            X+=mark
            print("X+",str(mark))
        elif k==3:
            b+=mark
            print("b+",str(mark))
        print("k=",k)
    print(a,"== a")
    print(X,"== X")
    print(b,"== b")
    return(a,X,b)
        

print("a[TX]b")
X=int(input("sisesta X: "))
a=float(input("sisesta a: "))
b=float(input("sisesta b: "))
avaldis=("("+str(a)+"[T"+str(X)+"]"+str(b)+")=")#teeb andmed avaldiseks
print("sulgude siseseim avaldis on:",leia_sulgude_siseseim_avaldis(avaldis))
print(leia_avaldisest_a_b_X(leia_sulgude_siseseim_avaldis(avaldis)))
