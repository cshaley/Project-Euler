#Euler Project #14
d = {}
def collatz(x,ct=1):
    if x%2==0:
        x=x/2
    else:
        x=3*x+1
    ct+=1
    if x == 1:
        return ct
    try:
        if d[x]:
            return d[x] + ct
    except:
        return collatz(x,ct)

for i in range(2,1000000):
    d[i] = collatz(i)
print max(d, key=d.get)