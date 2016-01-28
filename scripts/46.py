#Euler Problem 46
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

n=5800
global ps
ps = primesfrom2to(n)

def findgoldbach(x):
    for entry in ps:
        if entry < x:
            sq=1
            while 2*sq**2<x:
                if (entry + 2*sq**2) == x:
                    return True
                sq+=1
        else:
            break
    return False

x=[a for a in range(3,n,2) if a not in ps] 
for a in x:
    if not findgoldbach(a):
        print a