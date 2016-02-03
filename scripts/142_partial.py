#Euler Project #142
#I have no idea how to make this more efficient
#With maxnum=32, itertools created like 177M combinations, each of which have to be checked.  
import itertools
maxnum = 32
squares = set([a*a for a in range(maxnum)])
nums = range(1,maxnum**2)
combos = list(itertools.combinations(nums,3))
print len(combos)

for z,y,x in combos:
    lst = set([x+y,x-y,x+z,x-z,y+z,y-z])
    if len(lst.intersection(squares)) == 6:
        print x+y+z
