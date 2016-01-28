#Euler Problem 52
import collections
def samedigits(x,y):
    b=collections.Counter(str(x))
    arr=[1 for a in range(2,y+1) if b == collections.Counter(list(str(x*a)))]
    if len(arr) == y-1:
        return True
    return False
for i in range(1,10**8):
    if samedigits(i,6):
        print i
        break