#Euler Project #74
import math,time
def digitfactorialsum(x):
    x = str(x)
    return sum(math.factorial(int(a)) for a in x)
t=time.time()
dfs = {}
repeatingnums = set([1,169,363601,1454,871,45361,871,45362,872,145])
chainlengths = {1:1,169:3,363601:3,1454:3,871:2,45361:2,872:2,45362:2,145:1}

def findchainlength(x,numiter=0):
    if numiter>100:
        return -1
    try:
        s = dfs[x]
    except:
        s = digitfactorialsum(x)
        dfs[x] = s
    try:
        if chainlengths[s] > 0:
            return chainlengths[s] + numiter + 1
        else:
            return -1
    except:
        return findchainlength(s,numiter=numiter+1)


num=10**6

for x in range(1,num):
    dfs[x] = digitfactorialsum(x)

for x in range(10,num):
    if x not in repeatingnums:
        chainlengths[x] = findchainlength(x,numiter=0)

print chainlengths.values().count(60)
print "Program took " + str(time.time()-t) + " seconds!"
