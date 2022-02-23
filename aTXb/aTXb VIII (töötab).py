print("a[TX]b")
avaldis=[float(input("sisesta a: ")),int(input("sisesta X: ")),float(input("sisesta b: "))]
if avaldis[1]==2:
    avaldis=float(a_X_b[0])*float(a_X_b[2])
elif avaldis[1]==1:
    avaldis=float(a_X_b[0])+float(a_X_b[2])
def leia_sulgude_siseseim_avaldis(avaldis):#muudetud;töötab
    return(avaldis[len(avaldis)-3],avaldis[len(avaldis)-2],avaldis[len(avaldis)-1])
def lihtsusta_väikest_avaldist(a_X_b):
    if a_X_b[2]==1:
        a_X_b=a_X_b[0]
    else:
        a_X_b=[a_X_b[0],a_X_b[1]-1,a_X_b[0],a_X_b[1],(a_X_b[2]-1)]
    return(a_X_b)
def asenda_siseseimas_avaldises(avaldis,uus_a_X_b):
    avaldis=avaldis[:-3]
    if type(uus_a_X_b) is float:
        avaldis.append(uus_a_X_b)
    else:
        for m in uus_a_X_b:
            avaldis.append(m)
    return(avaldis)
while len(avaldis)!=1:
    a_X_b=(leia_sulgude_siseseim_avaldis(avaldis))
    print("sulgude siseseim avaldis on",a_X_b)
    if a_X_b[1]==3:
        uus_a_X_b=float(a_X_b[0])**float(a_X_b[2])
    else:
        uus_a_X_b=lihtsusta_väikest_avaldist(a_X_b)
    print("sulgude siseseim avaldis lihtsustatult on",uus_a_X_b)
    avaldis=asenda_siseseimas_avaldises(avaldis,uus_a_X_b)
    print("avaldis koos lihtsustatud lõpuga",avaldis,"\n")
print("vastus on",avaldis)
