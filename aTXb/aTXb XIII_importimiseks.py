def esita(a):
    b=str(a[0])
    for c in range(1,len(a)-1,2):
        b+=("[T"+str(a[c])+"]("+str(a[c+1]))
    return(b+")"*(len(a)//2))
def arvuta(a):
    while len(a)!=1:
        if a[len(a)-1]==1:
            a=a[:-3]+[a[len(a)-3]]
        if a[len(a)-2]==3:
            try:
                a=a[:-3]+[a[len(a)-3]**a[len(a)-1]]
            except MemoryError:
                return(b(a[:-2]+[3,a[len(a)-1]]))
        elif a[len(a)-2]==2:
            try:
                a=a[:-3]+[a[len(a)-3]*a[len(a)-1]]
            except MemoryError:
                return(b(a[:-2]+[2,a[len(a)-1]]))
        elif a[len(a)-2]==1:
            a=a[:-3]+[a[len(a)-3]+a[len(a)-1]]
        elif a[len(a)-2]==0:
            a=a[:-3]+[1]
        else:
            a=a[:-2]+[a[len(a)-2]-1,a[len(a)-3]]*(a[len(a)-1]-1)
    return(a)

def leia_sulgude_siseseim_avaldis(A):
    i=(A.index(")")-1)
    b=[]
    while A[i]!="(":
        print(A[i])
        
        i+=-1
    print(b)
    
print(esita([2,2,3,4,3,3,6]))
leia_sulgude_siseseim_avaldis("(3{T4}(2{T4}19)){T2}7")
