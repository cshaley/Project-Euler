#Euler Problem #69
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
num = 10**6
ps = primesfrom2to(num)
pfs = {}
for p in ps:
    pfs[p] = set([p])


def primefactors(x,fs=set()):
    for prime in ps:
        count=0
        while x % prime == 0:
            x /= prime
            count+=1
        if count > 0:
            fs.add(prime)
            try:
                return set.union(fs,pfs[x])
            except:
                pass
        if x == 1:
            return fs
    return 0
    
def totient(x):
    pfs[x] = set(primefactors(x,fs=set()))
    lst = [1-1./a for a in pfs[x]]
    return x*np.product(lst)

#This takes about 15.9 seconds
arr=[0]*(num-2)
for i in ps:
    arr[i-2] = i/(i-1)
import time
start_time=time.time()
for i in range(2,num):
    if arr[i-2]==0:
        arr[i-2] = i/totient(i)
print arr.index(max(arr))+2
print "Program took " + str(time.time()-start_time) + " seconds!"
