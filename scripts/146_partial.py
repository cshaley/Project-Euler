#Euler Project #146
#I have no idea how to do this. Even for the small part.  Requires primes above 10^12.  
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
#ps = primesfrom2to()
print "{:,}".format((150*10**6)**2)
potential_sqs = [10+a*30 for a in range(33333333333)]
potsqrts = [int(np.round(a**0.5)) for a in potential_sqs]
actsqrts = [potsqrts[ix] for ix in range(len(potsqrts))if potsqrts[ix]**2 == potential_sqs[ix] and (potential_sqs[ix]+27)%7!=0\
         and (potential_sqs[ix]+9)%7!=0 and (potential_sqs[ix]+3)%7!=0 and (potential_sqs[ix]+1)%7!=0 \
          and (potential_sqs[ix]+7)%7!=0 and (potential_sqs[ix]+27)%13!=0 and (potential_sqs[ix]+27)%17!=0]
print actsqrts
print sum(actsqrts)
