#Euler Project #119
def digitsum(x):
    return sum([int(a) for a in str(x)])

exps = set()
a=2
while a<150:
    a+=1
    b=1
    while a**b < 10**20:
        b+=1
        p = a**b
        if digitsum(p) == a:
            exps.add(p)
print sorted(exps)[29]
