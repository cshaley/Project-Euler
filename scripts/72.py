#Euler Problem #72
#for 8: 8,3,4,3,1,1
#for prime numbers, add the number - 1: e.g. 43 has 42 unique fractions
#for non-prime numbers, add 1 + the number of primes less than it.
import numpy as np
import pandas as pd
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
    
def totient(x):
    pfs[x] = primefactors(x,fs=[])
    lst = [1-1./a for a in pfs[x]]
    return x*np.product(lst)

#This took 13.5 minutes
import time
start_time = time.time()
arr=[0]*(10**6-1)
for i in ps:
    arr[i-2] = (i-1)
for i in range(2,10**6+1):
    if arr[i-2]==0:
        arr[i-2] = totient(i)
print sum(arr)
print time.time()-start_time
