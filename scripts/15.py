#Euler Problem 15
import math
def nCr(n,r):
    f = math.factorial
    return f(n)*1. / f(r) / f(n-r)

#You have 20 Rs and 20 Ds.  How many different orders can you combine them in?
#40 choose 20
print nCr(40,20)