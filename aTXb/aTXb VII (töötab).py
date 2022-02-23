def lihtsusta_väikest_avaldist(a_X_b):#muudetud
    a_X_b=[a_X_b[0],a_X_b[1]-1,[a_X_b[0],a_X_b[1],(a_X_b[2]-1)]]
    return(a_X_b)

def asenda_siseseimas_avaldises(su,milles,millega):#ei tööta!
   print("    milles:",milles)
   print("    sulusisesus on:",su)
   asendatult=millega
   return(asendatult)
    
def leia_sulgude_siseseim_avaldis(avaldis):#muudetud;töötab
    su=0
    while type(avaldis[2])==list:
        avaldis=avaldis[2]
        su+=1
    return(avaldis,su)

print("a[TX]b")
a_X_b=[float(input("sisesta a: ")),int(input("sisesta X: ")),float(input("sisesta b: "))]
i=0
while type(a_X_b)==list and i!=3:
    i+=1
    print("avaldis:",a_X_b)
    print("sulgude siseseim avaldis:",leia_sulgude_siseseim_avaldis(a_X_b)[0])
    if type(a_X_b[2])==float and a_X_b[1]==3:
        s2=(float(a_X_b[0])**float(a_X_b[2]))
        print("sulgude siseseima avaldise väärtus on:",s2)
        #peab nüüd asendama sulgude siseseima avaldise väärtuse sulgude siseima avaldise vastu
    else:
        s2=lihtsusta_väikest_avaldist(leia_sulgude_siseseim_avaldis(a_X_b)[0])
        print("sulgude siseseim avaldis lihtsustatult:",s2)
        #peab nüüd asendama sulgude siseseima avaldise lihtsustatult sulgude siseima avaldise vastu
    print("asendatava sulgude sisesus:",leia_sulgude_siseseim_avaldis(a_X_b)[1])
    print("asendaja:",s2)
    print("asendatav:",leia_sulgude_siseseim_avaldis(a_X_b))
    print("milles asendatakse:",a_X_b)
    su=leia_sulgude_siseseim_avaldis(a_X_b)[1]
    a_X_b=asenda_siseseimas_avaldises(su,a_X_b,s2)
    print("avaldis on tsükli lõpus: ",a_X_b,"\n")
print=("vastus on",a_X_b)
