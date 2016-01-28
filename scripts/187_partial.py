#Euler Problem #187
import itertools
from operator import mul
import time
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

#NOPE
start_time=time.time()
power = 4
x = primesfrom2to((10**power)/2)
y = len(set([a*b for a in x for b in x if a*b < 10**power])) #TOO SLOW at 10**5 (instant for 10^4, 10s for 10^5)
#y = [zip(a,x) for a in itertools.permutations(x,len(x))]# TOO SLOW at 10**2
#chain = itertools.chain(*y)
#y=set(list(chain))
#y = set([reduce(mul,a) for a in y])
print time.time()-start_time
print "n = " + str(10**power)