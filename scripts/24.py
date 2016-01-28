#Euler Project #24
import itertools
x = list(itertools.permutations('0123456789'))
print ''.join(x[999999])