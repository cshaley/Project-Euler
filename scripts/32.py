#Euler Project #32
def ispandigital(x):
    x=str(x)
    digits = list('123456789')
    if '0' in x:
        return False
    for i in digits:
        if x.count(i) != 1:
            return False
    return True

def digitsoverlap(x):
    try:
        x=''.join(str(a) for a in x)
    except:
        x=str(x)
    if '0' in x:
        return True
    for digit in x:
        if x.count(digit) != 1:
            return True
    return False

import itertools
p = itertools.permutations([x for x in range(1,5001) if not digitsoverlap(x)],2)
p = [a for a in p if not digitsoverlap(a)]
p = [(x[0],x[1],x[0]*x[1]) for x in p]
p = [a for a in p if ispandigital(a)]
prods = set(x[2] for x in p)
print sum(prods)