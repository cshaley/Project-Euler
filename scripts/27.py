#Euler Project #27
import numpy as np
import itertools
def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

ps1 = primesfrom2to(2*10**6)
ps = {}
for p in ps1:
    ps[p]=1
    
poss = [p for p in ps1 if p <1000]
poss = list(itertools.product(range(-999,999),poss))
maxct = 0
prod = 0
for tup in poss:
    i = 0
    while True:
        try: 
            if ps[(i**2 + tup[0]*i + tup[1])]:
                i += 1
        except:
            break
    if i > maxct:
        maxct=i
        prod = tup[0]*tup[1]
print prod
