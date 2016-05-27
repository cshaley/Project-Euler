#Euler Project #61
# Solution ran in 2.3ms
import itertools, sys, time
t = time.time()


# Only need numbers between 1k and 10k, 
# so anything ending in 00-09 cannot be cyclical
def meets_conditions(x):
    return(x < 10000 and x >= 1000 and x%100 >= 10)

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

# Beautiful, deep, nested for loop/if statements.
for order in itertools.permutations(range(6), 6):
    for firstnum in sets[order[0]]:
        firstnumback = int(str(firstnum)[2:])
        firstnumfront = int(str(firstnum)[0:2])
        if firstnumback in fronts[order[1]]:
            for secondnum in fronts[order[1]][firstnumback]:
                secondnumback = int(str(secondnum)[2:])
                if secondnumback in fronts[order[2]]:
                    for thirdnum in fronts[order[2]][secondnumback]:
                        thirdnumback = int(str(thirdnum)[2:])
                        if thirdnumback in fronts[order[3]]:
                            for fourthnum in fronts[order[3]][thirdnumback]:
                                fourthnumback = int(str(fourthnum)[2:])
                                if fourthnumback in fronts[order[4]]:
                                    for fifthnum in fronts[order[4]][fourthnumback]:
                                        fifthnumback = int(str(fifthnum)[2:])
                                        if fifthnumback in fronts[order[5]]:
                                            for sixthnum in fronts[order[5]][fifthnumback]:
                                                sixthnumback = int(str(sixthnum)[2:])
                                                if sixthnumback == firstnumfront:
                                                    print('Numbers: {0}, {1}, {2}, {3}, {4}, {5}\n').\
                                                        format(firstnum, secondnum, thirdnum, fourthnum, fifthnum, sixthnum)
                                                    print('SUM: {}').format(sum([firstnum, secondnum, thirdnum, fourthnum, fifthnum, sixthnum]))
                                                    print('TIME: {}').format(time.time()-t)
                                                    sys.exit(0)
