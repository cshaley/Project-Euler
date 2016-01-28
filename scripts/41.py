#Euler Problem #41
import numpy as np
def ispandigital(x):
    x=str(x)
    nums = ['1','2','3','4','5','6','7','8','9']
    for a in range(9-len(x)):
        nums.pop(-1)
    for num in nums:
        if num not in str(x):
            return False
    return True

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

ps = primesfrom2to(10**7)
for p in reversed(ps):
    if ispandigital(p):
        print p
        break