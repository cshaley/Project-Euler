from __future__ import division

import numpy as np
import fractions
import sys
sys.setrecursionlimit(1200)

sqrt2 = 1

#This is horribly slow because it recalculates all of the before parts 
#Also it reaches the maximum recursion depth at like 983, so I set the
# recursion depth higher
def sqrt2_recurse(count_recurse=0, recurse_limit=2):
    count_recurse += 1
    if count_recurse <= recurse_limit:
        a = 2 + fractions.Fraction(numerator=1, denominator=\
            sqrt2_recurse(count_recurse=count_recurse, recurse_limit=recurse_limit))
        return a
    else:
        return 2+fractions.Fraction(numerator=1, denominator=2)

cnt = 0
with open('txt.txt','w') as f:
    for i in range(1000):
        fract = sqrt2_recurse(recurse_limit=i)-1
        if len(str(fract.numerator))>len(str(fract.denominator)):
            cnt+=1
            f.write(str(cnt))
        print i
        
print cnt
