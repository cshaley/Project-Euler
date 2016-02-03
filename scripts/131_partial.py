#Euler Project #131
import numpy as np
import itertools
import bisect
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
plen = len(ps)
cubes = [a**3 for a in range(1,int((10**12)**(1.0/3))+1)]
print len(cubes)
pcp = []
x = list(itertools.combinations(cubes,2))
x = [(min(a,b),max(a,b)) for a,b in x if min(a,b)*ps[-1]>=max(a,b)]
print len(x)
t = time.time()
for a,b in x:
    #approximate prime number
    y = (b-a)*(a**(-2/3.0))
    #print str(y) + "    " +str(y%1)
    #if y%1 <.01 or y%1>.99:
    y=int(np.round(y))
    #print ""
    #print "y = " +str(y)
    #print "formula = " + str(a+int(np.round(a**(2.0/3)))*y)
    #print "a = " + str(a)
    #print "b = " + str(b)
    #print "formula = b?: " + str(a+int(np.round(a**(2.0/3)))*y == b)
    if a+int(np.round(a**(2.0/3)))*y == b:
        yloc = bisect.bisect_left(ps,y)
        if yloc<plen:
            #print "\ny = " + str(y)
            #print "y index = " + str(yloc)
            #print "num at y index = " + str(ps[yloc])
            #print "prime y: " + str(ps[yloc])
            if ps[yloc] == y:
                #print "a: "+ str(a) + "   b: "+str(b)+ "   y: "+str(y)
                pcp.append(y)
print pcp
print "Search took "+ str(time.time()-t) + " seconds to complete." 
