#Euler Problem #58
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

n=10**9
global ps
ps = set(primesfrom2to(n))

#I shouldn't remake this every time
# I should append to the lists every iteration.

def spiralprimepercentage(size):
    squares = [a**2 for a in range(1,size+1,2)]
    lr=[]
    for ix, a in enumerate(squares):
        lr.append(a+((ix+1)*2))
    lr.pop(-1)
    ll=[]
    for ix, a in enumerate(squares):
        ll.append(a+((ix+1)*4))
    ll.pop(-1)
    ul=[]
    for ix, a in enumerate(squares):
        ul.append(a+((ix+1)*6))
    ul.pop(-1)
    out=set(ul+ll+lr+squares)
    psinout = set(out).intersection(ps)
    return len(psinout)*1./len(out)
x=7
while spiralprimepercentage(x)>0.1:
    x+=2
    if x**2>n:
        print "broken"
        break
print x