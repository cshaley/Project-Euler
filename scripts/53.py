#Euler Problem #53
import math
def nCr(n,r):
    f = math.factorial
    return f(n)*1. / f(r) / f(n-r)
import itertools
x = list(itertools.permutations(range(101),2))
x = [a for a in x if a[1]<=a[0]]
x = [nCr(a[0],a[1]) for a in x]
x = [a for a in x if a>1000000]
print len(x)