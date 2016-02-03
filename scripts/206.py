#Euler Project #206
#ends in 30, maybe 8030
import numpy as np
concealtester = [9,8,7,6,5,4,3,2,1]
def isconcealedsq(x):
    for i in range(9):
        if x%10==concealtester[i]:
            x/=100
        else:
            return False
    return True
x0 = int(1.01010101*10**8)
y0 = int(1.41421*10**8)
#x = (x0)**2
#y = (y0)**2
#print "{:,}".format(x)
#print "{:,}".format(y)
#print y0-x0

for n in range(x0,y0,2):
    if isconcealedsq(n*n):
        print n*10
        break
