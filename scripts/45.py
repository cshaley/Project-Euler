#Euler Problem 45
#Check every number to see if it's hexagonal
#if it is, check if it is pentagonal
#if it is, check if it is triangular
​
def tri(x):
    return x*(x+1)/2.
def pent(x):
    return x*(3*x-1)/2.
def hexm(x):
    return x*(2*x-1)
​
tris=[]
pents=[]
hexes=[]
for i in range(100000):
    tris.append(tri(i))
    pents.append(pent(i))
    hexes.append(hexm(i))
t1 = pd.DataFrame(tris)
t2 = pd.DataFrame(pents)
t3 = pd.DataFrame(hexes)
print int(pd.merge(pd.merge(t1,t2,on=[0]),t3,on=[0]).max(0))