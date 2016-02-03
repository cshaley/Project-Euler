#Euler Project #145
#Takes 15 minutes - could be sped up at least in half by noting which numbers have been reversed
import time
import sys

def isreversible(x):
    if x%10==0:
        return False
    y = int(str(x)[::-1])
    x = x+y
    while x>0:
        if x%2 ==0:
            return False
        x/=10
    return True

t = time.time()
ct = 0
for j in range(10):
    for i in range(j*10**8,(j+1)*10**8):
        if isreversible(i):
            ct+=1
print ct
print "Program took "+ str(time.time()-t) + " seconds to complete." 
