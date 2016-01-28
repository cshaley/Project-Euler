#Euler Project #23
def factors(n):    
    a = set(reduce(list.__add__,([i, n/i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    a.remove(n)
    return a
abunds=[x for x in range(12,28123) if sum(factors(x))>x]
import itertools
absums = set(sum(x) for x in list(itertools.combinations_with_replacement(abunds,2)) if sum(x) <= 28123)
print sum(set(range(1,28124))-absums)