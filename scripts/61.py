#Euler Project #61
# Solution ran in 2.3ms
import itertools, sys, time
t = time.time()


# Only need numbers between 1k and 10k, 
# so anything ending in 00-09 cannot be cyclical
def meets_conditions(x):
    return(x < 10000 and x >= 1000 and x%100 >= 10)

# Get digits 3 onward of number
def back(x):
    return int(str(x)[2:])

# Get front two digits of number
def front(x):
    return int(str(x)[0:2])


triangles = [x*(x+1)/2 for x in range(200) if meets_conditions(x*(x+1)/2)]
squares = [x**2 for x in range(200) if meets_conditions(x**2)]
pentagonals = [x*(3*x-1)/2 for x in range(200) if meets_conditions(x*(3*x-1)/2)]
hexagonals = [x*(2*x-1) for x in range(200) if meets_conditions(x*(2*x-1))]
heptagonals = [x*(5*x-3)/2 for x in range(200) if meets_conditions(x*(5*x-3)/2)]
octagonals = [x*(3*x-2) for x in range(200) if meets_conditions(x*(3*x-2))]

sets = [triangles, squares, pentagonals, hexagonals, heptagonals, octagonals]
fronts = []

# Make a dictionary mapping front 2 numbers to all numbers matching that desc
# in each group.
for s in sets:
    fs = {}
    for num in range(10,100):
        a = set([i for i in s if int(str(i)[0:2]) == num])
        if len(a) > 0:
            fs[num] = a
    fronts.append(fs)


def recurse(sets, fronts, order, orderind=0, numbacklist=None):
    if numbacklist is None:
        numbacklist = []
        for firstnum in sets[order[orderind]]:
            firstnumback = back(firstnum)
            if firstnumback in fronts[order[orderind+1]]:
                ret = recurse(sets, fronts, order, orderind+1, numbacklist=[firstnum])
                if ret is not None:
                    return ret
    else:
        if orderind == 5:
            firstnumfront = front(numbacklist[0])
            for sixthnum in fronts[order[orderind]][back(numbacklist[-1])]:
                sixthnumback = back(sixthnum)
                if firstnumfront == sixthnumback:
                    numbacklist.append(sixthnum)
                    return numbacklist
        else:
            for midnum in fronts[order[orderind]][back(numbacklist[-1])]:
                midnumback = back(midnum)
                if midnumback in fronts[order[orderind+1]]:
                    return recurse(sets, fronts, order, orderind+1, numbacklist=numbacklist+[midnum])
    return None

if __name__ == '__main__':
    for order in itertools.permutations(range(6), 6):
        x = recurse(sets, fronts, order, orderind=0, numbacklist=None)
        if x:
            print('Numbers: {}').format(x)
            print('SUM: {}').format(sum(x))
            print('TIME: {}').format(time.time()-t)
            break
