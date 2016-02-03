#Euler Project #134
import numpy as np
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
ps = list(primesfrom2to(10**4))
ps.pop(0)
ps.pop(0)

def findprimepairconnection(p1,p2):
    x=p2
    while True:
        x += p2
        if str(x).endswith(str(p1)):
            return x

sum1 = 0
for p in range(len(ps)-1):
    p1 = ps[p]
    p2 = ps[p+1]
    sum1 += findprimepairconnection(p1,p2)
print sum1
