#Euler Project #61
triangles = [x*(x+1)/2 for x in range(200) if x*(x+1)/2 < 10000 and x*(x+1)/2 >= 1000]
squares = [x**2 for x in range(200) if x**2 < 10000 and x**2 >= 1000]
pentagonals = [x*(3*x-1)/2 for x in range(200) if x*(3*x-1)/2 < 10000 and x*(3*x-1)/2 >= 1000]
hexagonals = [x*(2*x-1) for x in range(200) if x*(2*x-1) < 10000 and x*(2*x-1) >= 1000]
heptagonals = [x*(5*x-3)/2 for x in range(200) if x*(5*x-3)/2 < 10000 and x*(5*x-3)/2 >= 1000]
octagonals = [x*(3*x-2) for x in range(200) if x*(3*x-2) < 10000 and x*(3*x-2) >= 1000]
sets=[triangles,squares,pentagonals,hexagonals,heptagonals,octagonals]

fronts = {}
backs = {}
inters = {}
#for all 90 numeric possibilities, get a list of indices in array which match
for num in range(10,100):
    fronts[num] = set([(i,j) for i in range(len(sets)) for j in range(len(sets[i])) if int(str(sets[i][j])[0:2]) == num])
    backs[num] = set([(i,j) for i in range(len(sets)) for j in range(len(sets[i])) if int(str(sets[i][j])[-2:]) == num])

def findcycles(cyclesofar):
    if len(cyclesofar) == 6:
        return cyclesofar
    possible_nexts = fronts[int(str(cyclesofar[-1])[-2:])]
#I have no idea what I'm doing.    
findcycles([35])
print fronts[35]