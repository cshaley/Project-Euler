#Euler Project #87
import numpy as np, itertools
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

sqps = primesfrom2to(int((50*10**6)**(1./2)))
cubps = primesfrom2to(int((50*10**6)**(1./3)))
fourthps = primesfrom2to(int((50*10**6)**(1./4)))
prod = list(itertools.product(*[sqps,cubps,fourthps]))
nums = set()
for tup in prod:
    x = tup[0]**2+tup[1]**3+tup[2]**4
    if x<50*10**6:
        nums.add(x)
print len(nums)
