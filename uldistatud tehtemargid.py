def f(a,g,b):
    if b==1:
        return(g(a))
    return(g(f(a,g,b-1)))

def g_0(x):
    return(x+1)
print(f(3,g_0,4))


def g_1(x):
    return(f(x,g_0,x))
print(f(3,g_1,4))


#def g_2(x):
#    return (x*x)
#print(f(3,g_2,4/2))