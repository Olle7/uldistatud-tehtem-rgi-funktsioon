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
        if Sid[indeks]!=max(Sid):
            break
            print("break")
        sulgude_siseseim_avaldis+=list(avaldis)[indeks]#vastava indeksiga täht liida avaldisse
    return(sulgude_siseseim_avaldis)
def leia_avaldisest_a_b_X(avaldis):
    k=0
    a=""
    b=""
    X=""
    for mark in(list(avaldis)):
        if mark.isdigit() is False and mark != "." :#kui mõni märk pole number või "." siis k +=1
            k+=1
        elif k==0:#kui k==0 siis numbrid või "." tähendavad a´d
            a+=mark
        elif k==2:#kui k==2 siis numbrid või "." tähendavad X´i
            X+=mark
        elif k==3:#kui k==3 siis numbrid või "." tähendavad b´d
            b+=mark
    return(a,X,b)
def lihtsusta_b(avaldis):
    try:
        a=float(leia_avaldisest_a_b_X(avaldis)[0])
    except:
        TypeError
        a=(leia_avaldisest_a_b_X(avaldis)[0])
    try:
        b=float(leia_avaldisest_a_b_X(avaldis)[2])
    except:
        TypeError
        b=(leia_avaldisest_a_b_X(avaldis)[2])
    X=int(leia_avaldisest_a_b_X(avaldis)[1])
    if type(b)==float:#kui b on arv siis lahuta temast 1
        B=b-1
    else:
        print("b on avaldis")
        b="("+b+")"
        B=b+"[T1]-1"#kui b pole arv kirjuta b asemele b-1
    X_miinus_1=(str(a)+"[T"+str(X-1)+"]("+str(leia_avaldisest_a_b_X(avaldis)[0])+"[T"+str(X)+"]"+str(B)+")")
    return(X_miinus_1)
print("a[TX]b")
X=int(input("sisesta X: "))
a=float(input("sisesta a: "))
b=float(input("sisesta b: "))
avaldis=("("+str(a)+"[T"+str(X)+"]"+str(b)+")=")#teeb andmed avaldiseks
print("avaldis on",avaldis)
print("sulgude siseseim avaldis on:",leia_sulgude_siseseim_avaldis(avaldis))
print("lihtsustatumalt on avaldis",lihtsusta_b(leia_sulgude_siseseim_avaldis(avaldis)))
