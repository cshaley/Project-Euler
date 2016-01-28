#Euler Problem #49
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

def same4nums(x,y):
    return sorted(list(str(x))) == sorted(list(str(y)))

ps = np.array(primesfrom2to(10**4))[168:]
psd={}
for p in ps:
    psd[p]=1
keys=psd.keys()
for ix, p in enumerate(keys):
    for i in range(ix+1,len(keys)):
        if same4nums(keys[i],p):
            try:
                if psd[keys[i]+abs(keys[i]-p)] and same4nums(keys[i]+abs(keys[i]-p),p) \
                                    and len(set([p,keys[i],keys[i]+abs(keys[i]-p)]))==3:
                    print str(p)+' '+str(keys[i])+' '+str(keys[i]+abs(keys[i]-p))
            except:
                pass