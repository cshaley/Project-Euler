#Euler Problem #381
import math
def s(x):
    r=0
    for i in range(1,6):
        r += math.factorial(x-i)
    #print str(x) + '    '+str(r)+ '  '+str(r%x)
    return r%x
arr=[]
for i in range(5,10**2):
    arr.append(s(i))
print arr
print len(arr)
print sum(arr)
#should be 480??? but is 489