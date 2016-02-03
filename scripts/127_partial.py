#Euler Project #127
#Create all possible ab pairs for every given c on the condition a+b=c where a<b
#Note: Pairs always have a perfect square (or cube, etc.) or a prime
#
#Check each pair for common denominators (eliminate unwanted pairs)
#Calculate rad(abc)
import time
import numpy as np
from fractions import gcd
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

ps = primesfrom2to(10**5*1.2)
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

def rad(n):
    return np.product(primefactors(n,fs=[]))

def expsbelow(n):
    exps = set()
    for i in range(2,int(n**0.5)+1):
        pow1 = 2
        pl = 1
        while pl < n:
            pl = i**pow1
            if pl < n:
                exps.add(pl)
            pow1 += 1
    return list(exps)

def primesandexpsbelow(n):
    p1 = list(primesfrom2to(n))
    exps = expsbelow(n)
    return sorted([1]+p1+exps)

num = 10**3
pre = primesandexpsbelow(num)
t = time.time()

abc_hits = set()
for c in sorted(expsbelow(num)):
    if c%2==0:
        a = range(1,c/2)
    else:
        a = range(1,c/2+1)
    b = range(c-1,c/2,-1)
    for i in range(len(a)):
        if gcd(a[i],b[i]) == 1:
            if gcd(a[i],c) == 1:
                if gcd(b[i],c) == 1:
                    if rad(a[i]*b[i]*c) < c:
                        #print str(a[i])+' + ' + str(b[i]) + ' = ' + str(c)
                        abc_hits.add((a[i],b[i],c))
for ix,a in enumerate(pre):
    for b in pre[ix:len(pre)-1]:
        if a+b<num:
            c = a+b
            if gcd(a,b) == 1:
                if gcd(a,c) == 1:
                    if gcd(b,c) == 1:
                        if rad(a*b*c) < c:
                            #print str(a)+' + ' + str(b) + ' = ' + str(c)
                            abc_hits.add((a,b,c))
print sum(a[2] for a in abc_hits)
print "It took " + str(time.time()-t) + " seconds to complete."
