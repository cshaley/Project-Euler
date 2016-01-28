#Euler Project Problem 50
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

ps = primesfrom2to(10**6)
psums = []
maxlen=6
for i in range(len(ps)):
    for j in range(i+maxlen,int(len(ps)**.6)):
        mp = sum(ps[i:j])
        if mp in ps:
            if j-i > maxlen:
                maxlen = j-i
                maxprime = mp
print maxlen
print maxprime