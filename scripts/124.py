#Euler Project #124
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

ps = primesfrom2to(10**5)
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

d = {1:1}
for i in range(2,10**5+1):
    d[i] = np.product(primefactors(i,fs=[]))
#    if i %10000 == 0:
#        print i
        
x = pd.DataFrame([d.keys(),d.values()]).transpose()
x = x.rename(columns={0: 'n', 1: 'rad(n)'})
x = x.sort(columns=['rad(n)','n']).reset_index()
del x['index']
x = x.reset_index()
x = x.rename(columns={'index': 'k'})
x = x[['n','rad(n)','k']]
x['k'] = x['k'] + 1

print x[x['k']==10000]['n']
