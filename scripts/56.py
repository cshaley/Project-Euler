#Euler Problem 56
import itertools
x = list(itertools.permutations(range(1,100),2))
x = [a[0]**a[1] for a in x]
for ix,entry in enumerate(x):
    es=0
    while entry:
        digit = entry % 10
        es+=digit
        entry /= 10
    x[ix]=es
print max(x)