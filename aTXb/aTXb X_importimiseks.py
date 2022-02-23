def arvuta(a):
    if (len(a)-1)%2!=0:
        quit("Liikmete arv ei sobi\nnt:[a,b,c,d,e,f,g]=a[Tb](c[Td](e[Tf]g))")
    if a[1]==2:
        return(a[0]*a[2])
    elif a[1]==1:
        return(a[0]+a[2])
    elif a[1]==0:
        return(1)
    while len(a)!=1:
        if a[len(a)-1]==1:
            b=a[len(a)-3]
            a=a[:-2]
            a[len(a)-1]=b
        elif a[len(a)-2]==3:#peax if a[len(a)-1]==1:´ga vahetuses olema? 
            b=a[len(a)-3],a[len(a)-1]#mis juhtub kui mõlemad on samad?
            a=a[:-2]
            try:
                a[len(a)-1]=b[0]**b[1]
            except OverflowError:
                return(a+[b[0],b[1]])
        else:
            b=a[len(a)-1],a[len(a)-2],a[len(a)-3]
            a=a[:-3]
            a+=[b[2],b[1]-1,b[2],b[1],b[0]-1]
    return(a[0])
print(arvuta([3,4,3,3,3]))
