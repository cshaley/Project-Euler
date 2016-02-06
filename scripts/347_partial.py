#Euler Project #347
#Ways to approach this
#For every prime combination p,q: work back from 10M and find first number whose prime factors are only p and q
#For every prime combination p,q: generate every possible multiplicative combination below 10M and take max.
#Find prime factors of every number from 1 to 10M -> store in dictionary.  dict[factorlist] = largest generated number
            # e.g. dict[[2,3]]= 6, then when you check 12, dict[[2,3]] = 12 etc.
# I tried the third approach.  This will not work.  10^7 is way too big.  27 seconds for 10**5. --> approx 18.75 hours for 10**7
import numpy as np
import time
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
pfs = {}

def primefactors(x,fs=[]):
    for prime in ps:
        count=0
        while x % prime == 0:
            x /= prime
            count+=1
        if count > 0:
            fs.append(prime)
            try:
                return list(set(fs+pfs[x]))
            except:
                pass
        if x == 1:
            return fs
    return 0
t = time.time()
for i in range(2,10**2+1):
    x = primefactors(i,fs=[])
    if len(x) == 2:
        pfs[np.product(x)] = i
print sum(pfs.values())
print "Program took "+ str(time.time()-t) + " seconds to complete." 
