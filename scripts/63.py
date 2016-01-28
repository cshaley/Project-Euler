#Euler Problem 63
import itertools
x = list(itertools.product(range(1,22),repeat=2))
x = [a for a in x if a[0]<10]
x = [a for a in x if len(str(a[0]**a[1]))==a[1]]
print len(x)