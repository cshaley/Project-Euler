#Euler Project #21
def factors(n):    
    a = set(reduce(list.__add__,([i, n/i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    a.remove(n)
    return a
d={}
for i in range(2,10000):
    d[i]=sum(factors(i))
for x in d.keys():
    if d[x] == x:
        del d[x]
    elif True:
        try:
            if d[d[x]] != x:
                del d[x]
        except:
            del d[x]
print sum(d.keys())