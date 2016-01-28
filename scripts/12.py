#Euler Project #12
#factors function taken from stackoverflow
def factors(n):    
    return set(reduce(list.__add__, 
                ([i, n/i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))

x=0
for i in range(1,100000):
    x+=i
    if len(factors(x))>500:
        print x
        break