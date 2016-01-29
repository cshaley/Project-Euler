#Euler Project #95
def factors(n):    
    a = set(reduce(list.__add__,([i, n/i] for i in range(1, int(n**0.5) + 1) if n % i == 0)))
    a.remove(n)
    return a

def findamicablechainlength(x,y=set([x]),prevnum=x,ct=0):
    ct += 1
    prevnum = factorsumdict[prevnum]
    ylen = len(y)
    y.add(prevnum)
    
    if prevnum == 1:
        return -1,[]
    elif prevnum == x:
        return ct,y
    elif prevnum > 10**6:
        return -1,[]
    elif ylen == len(y):
        return -1,[]
    else:
        return findamicablechainlength(x,y,prevnum,ct)

factorsumdict = {1:1}
loopdict = {}
for i in range(2,10**6):
    factorsumdict[i] = sum(factors(i))

for x in factorsumdict.keys():
    if factorsumdict[x] == x:
        loopdict[x] = 1
    else:
        try:
            if loopdict[x]:
                pass
        except:
            length, members = findamicablechainlength(x,set([x]),x,0)
            for member in members:
                loopdict[member] = length
maxchainlength = max(loopdict.values())
numwithmaxchainlength = max(loopdict, key=loopdict.get)
a,maxchain = findamicablechainlength(numwithmaxchainlength,set([numwithmaxchainlength]),numwithmaxchainlength,0)
print min(maxchain)
