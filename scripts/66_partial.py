#Euler Project #66
#Incomplete.  Takes too long to do it all.  15 minutes as is, and it doesn't find x for many Ds.  eg 61
#Only iterates up to x=10**6
#x^2-Dy^2=1
#x^2 = 1 + Dy^2
import time
t = time.time()
maxsq = 10**6
squares = set([a*a for a in range(1,maxsq)])
sqs = {}
for a in squares:
    sqs[a] = 1
    
Ds = range(2,10**3)
DsDict = {}
Ds = [d for d in Ds if d not in squares]
for d in Ds:
    DsDict[d] = 0


for d in Ds:
    minx = maxsq**2
    for y in sqs.keys():
        xsq = 1+d*y
        try:
            if sqs[xsq]:
                if xsq < minx:
                    minx = xsq
        except:
            pass
    DsDict[d] = int(minx**0.5)
#print DsDict
print max(DsDict, key=DsDict.get)
print "Program took "+ str(time.time()-t) + " seconds to complete." 
