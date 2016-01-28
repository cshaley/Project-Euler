#Euler Problem 47
def primefactors(n):
    divisors = [ d for d in range(2,n/2+1) if n % d == 0 ]
    return [ d for d in divisors if \
             all( d % od != 0 for od in divisors if od != d ) ]
pf=[]
consec=0
for i in range(130000,150000):
    x = primefactors(i)
    if len(x)==4:
        pf.append(i)
        consec+=1
        if consec==4:
            break
    else:
        consec=0
pf[-4:]