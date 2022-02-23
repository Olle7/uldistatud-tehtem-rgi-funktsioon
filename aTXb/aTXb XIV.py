a=[int(input("a[TX]b\nSisesta täisarv a:")),abs(int(input("Sisesta naturaalarv X:"))),int(input("Sisesta naturaalarv b:"))]#küsib sisenedeid
print(str(a[0])+"[T"+str(a[1])+"]"+str(a[2])+"=")#kuvab avaldise,kuhu on asendatud väätused
if a[1]==2:#kui X==2
    a=[a[0]*a[2]]#on tegemist korrutamisega
elif a[1]==1:#kui X==1
    a=[a[0]+a[2]]#on tegemist liitmisega
elif a[1]==0:#kui X==0
    a=[1]#on vastus alati 1
def b(a):#tagastab esituse avaldisesele kergelt loetavalt
    b=str(a[0])#paneb avaldise kirjaliku kuju algusese 1. arvu millega hakatakse tehet sooritama
    for c in range(1,len(a)-1,2):#iga teise arvu,mis on X´id, kohta loendis
        b+=("[T"+str(a[c])+"]("+str(a[c+1]))#lisab avaldise kirajalikule kujule "[T"+X+"]("+b
    return(b+")"*(len(a)//2))#lõpu sulge on vaja kaks korda ja ühe võrra vähem ,kui on avaldises arve  
while len(a)!=1:#kuni pole alles ainult 1 arv avaldises
    if a[len(a)-1]==1:#kui viimane arv on 1,!!!(lihtsustus 2)
        a=a[:-3]+[a[len(a)-3]]#siis arvutab ja asendab viimase 3´e liikmelise avaldise ehk A[TX]B==A[TX]1=A nt:2[T4](3[T4](13[T5]1))=2[T4](3[T4]13)
    if a[len(a)-2]==3:#kui b on kolm on vaja astendada
        try:#proovib sooritada viimase kolme liikmega tehet,kuna X==3 ,siis on see astendamine(lihtsustus 3)
            if a[len(a)-1]>2000:#kui astendaja>2000,
                print(str(b(a))+"=")#siis enne astendamist kuvab avaldise nt:[9,3,387420489]=9[T3](387420489)
            a=a[:-3]+[a[len(a)-3]**a[len(a)-1]]#asendab viimased 3 astendamise tulemusega.nt:2[T4](3[T4](2[T3]3))=2[T4](3[T4]8)
        except MemoryError:#kui arvutamisel tuleb veateade
            print(b(a[:-2]+[3,a[len(a)-1]]))#,siis esitab avaldise milleni õnnestus arvutada
            quit("Tekib liiga raske arvutus edasi arvutamaks.")#ja quid´ib
    elif 1000>a[len(a)-1]:#kui viimane arv avaldises<2000,sest muidu jookseb arvuti kokku(lihtustus 3)
        a=a[:-2]+[a[len(a)-2]-1,a[len(a)-3]]*(a[len(a)-1]-1)#viib avaldise 1võrra madalamale tehtemärgile ehk X=X-1 nt:3[T4](2[T5]4)=3[T4](2[T4](2[T4](2[T4]2)))
    else:#kui 1võrra madalamale tehtemärgile viimisel tekib enam kui 2000 arvu lisamise vajadus 
        print(b(a))#,siis esitab avaldise milleni õnnestus arvutada nt:[2,4,1001]=2[T4]1001
        quit("Tekib liiga raske arvutus edasi arvutamaks.")#ja quid´ib
print(a[0])#kuvab lõpliku vastuse
