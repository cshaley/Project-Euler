#Euler Project #37
#[37,73,797,3797,23,373,]
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

ps=primesfrom2to(10**6)
def istruncatable(x,ps):
    x=str(x)
    for i in range(len(x)):
        if int(x[i:]) not in ps:
            return False
        if int(x[:len(x)-i]) not in ps:
            return False
    return True
tps=[]
for p in ps:
    if istruncatable(p,ps):
        tps.append(p)
tps.pop(0)
tps.pop(0)
tps.pop(0)
tps.pop(0)
print tps
print sum(tps)