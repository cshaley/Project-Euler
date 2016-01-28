#Euler Project #39
def findtris(x):
    tris=set()
    a = 1
    b = 1
    while x>a+x/2:
        b=1
        while x>a+b:
            if (a**2 + b**2 == (x-a-b)**2):
                tris.update((a,b,x-a-b))
            b+=1
        a+=1
    return tris
d={}
for i in range(10,1001):
    d[i]=len(findtris(i))
print max(d, key=d.get)