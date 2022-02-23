a=[int(input("a[TX]b\nSisesta a:")),abs(int(input("Sisesta naturaalarv X:"))),int(input("Sisesta b:"))]
print(str(a[0])+"[T"+str(a[1])+"]"+str(a[2])+"=")
if a[1]==2:#kui X==2
    a=[a[0]*a[2]]#on tegemist korrutamisega
elif a[1]==1:#kui X==1
    a=[a[0]+a[2]]#on tegemist liitmisega
elif a[1]==0:#kui X==0
    a=[1]
def b(a):#tagastab esituse avaldisesele kergelt loetavalt
    b=str(a[0])
    for c in range(1,len(a)-1,2):
        b+=("[T"+str(a[c])+"]("+str(a[c+1]))
    return(b+")"*(len(a)//2))#lõpu sulge on vaja kaks korda ja ühe võrra vähem ,kui on avaldises arve  
while len(a)!=1:#kuni pole alles ainult 1 nr avaldises
    if a[len(a)-1]==1:#kui b on 1 ,siis a[TX]b==a[TX]1==a
        a=a[:-3]+[a[len(a)-3]]#nt:2[T4](3[T4](13[T5]1))==2[T4](3[T4]13)
    if a[len(a)-2]==3:#kui b on kolm on vaja astendada
        try:#proovib sooritada viimase kolme liikmega tehet,kuna X==3 ,siis on see astendamine
            if a[len(a)-1]>2000:#kui astendaja > 2000,
                print(str(b(a))+"=")#siis enne astendamist prindi avaldis
            a=a[:-3]+[a[len(a)-3]**a[len(a)-1]]#asendab viimased 3 astendamise tulemusega.nt:2[T4](3[T4](2[T3]3))=2[T4](3[T4]8)
        except(OverflowError,MemoryError):#kui arvutamisel tuleb veateade
            print(b(a[:-2]+[3,a[len(a)-1]]))#,siis esitab avaldise milleni õnnestus arvutada
            quit("Tekib liiga raske arvutus edasi arvutamaks.")#ja quid´ib
    elif 2000>a[len(a)-1]:#kui viimane arv avaldises<2000,sest muidu jookseb arvuti kokku
        a=a[:-2]+[a[len(a)-2]-1,a[len(a)-3]]*(a[len(a)-1]-1)#viib avaldisse 1võrra madalamale tehtemärgile ehk X=X-1 nt:3[T4](2[T5]4))=3[T4](2[T4](2[T4](2[T4]2))))
    else:
        print(b(a))#esitab avaldise milleni õnnestus arvutada
        quit("Tekib liiga raske arvutus edasi arvutamaks.")#ja quid´ib
print(a[0])#prindi lõplik vastus
