def kuva_avaldis_üldistatud_tehtemärgina(a):# tagastab esituse avaldisesele kergelt loetavalt
    b=str(a[0])# paneb avaldise kirjaliku kuju algusese 1. arvu millega hakatakse tehet sooritama
    for c in range(1,len(a)-1,2):# iga teise arvu,mis on X´id, kohta loendis
        b+=("[T"+str(a[c])+"]("+str(a[c +1]))# lisab avaldise kirajalikule kujule "[T"+X+"]("+b
    return (b+")"*(len(a)//2))# lõpu sulge on vaja kaks korda ja ühe võrra vähem ,kui on avaldises arve
def kuva_avaldis_funktsioonina(a):
    if type(a)==int or type(a)==str:
        return (a)
    if type(a[0])!=list and type(a[1])!=list and type(a[2])!=list:
        return ("f("+str(a[0])+";"+str(a[1])+";"+str(a[2])+")")
    return (kuva_avaldis_funktsioonina([kuva_avaldis_funktsioonina(a[0]), kuva_avaldis_funktsioonina(a[1]), kuva_avaldis_funktsioonina(a[2])]))
def arvuta_f(a):
    if a[1]==2:#kui X==2
        a=[a[0]*a[2]]#on tegemist korrutamisega
    elif a[1]==1:#kui X==1
        a=[a[0]+a[2]]#on tegemist liitmisega
    elif a[1]==0:#kui X==0
        a=[1]#on vastus alati 1
    while len(a)!=1:#kuni pole alles ainult 1 arv avaldises
        if a[len(a)-1]==1:#kui viimane arv on 1,!!!(lihtsustus 2)
            a=a[:-3]+[a[len(a)-3]]#siis arvutab ja asendab viimase 3´e liikmelise avaldise ehk A[TX]B==A[TX]1=A nt:2[T4](3[T4](13[T5]1))=2[T4](3[T4]13)
        if a[len(a)-2]==3:#kui b on kolm on vaja astendada
            try:#proovib sooritada viimase kolme liikmega tehet,kuna X==3 ,siis on see astendamine(lihtsustus 3)
                if a[len(a)-1]>2000:#kui astendaja>2000,
                    print(str(kuva_avaldis_üldistatud_tehtemärgina(a)) + "=")#siis enne astendamist kuvab avaldise nt:[9,3,387420489]=9[T3](387420489)
                a=a[:-3]+[a[len(a)-3]**a[len(a)-1]]#asendab viimased 3 astendamise tulemusega.nt:2[T4](3[T4](2[T3]3))=2[T4](3[T4]8)
            except MemoryError:#kui arvutamisel tuleb veateade
                return(kuva_avaldis_üldistatud_tehtemärgina(a[:-2] + [3, a[len(a) - 1]]))#,siis esitab avaldise milleni õnnestus arvutada
        elif 1000>a[len(a)-1]:#kui viimane arv avaldises<2000,sest muidu jookseb arvuti kokku(lihtustus 3)
            a=a[:-2]+[a[len(a)-2]-1,a[len(a)-3]]*(a[len(a)-1]-1)#viib avaldise 1võrra madalamale tehtemärgile ehk X=X-1 nt:3[T4](2[T5]4)=3[T4](2[T4](2[T4](2[T4]2)))
        else:#kui 1võrra madalamale tehtemärgile viimisel tekib enam kui 2000 arvu lisamise vajadus
            return(kuva_avaldis_üldistatud_tehtemärgina(a))#,siis esitab avaldise milleni õnnestus arvutada nt:[2,4,1001]=2[T4]1001
    return(a[0])#kuvab lõpliku vastuse
def arvuta_avaldis_f(a):
    if type(a)==int:
        return(a)
    if type(a[0])==int and type(a[1])==int and type(a[2])==int:
        return(arvuta_f(a))
    return(arvuta_avaldis_f([arvuta_avaldis_f(a[0]),arvuta_avaldis_f(a[1]),arvuta_avaldis_f(a[2])]))
#def lihtsusta_tundmatutega_avaldist(a):
#
print(arvuta_avaldis_f([1,1,[3,4,2]]))
#print(arvuta_avaldis_f([3,1,[3,4,5]]))