from __future__ import division
from fractions import gcd
import numpy as np

s = 0
for denom in range(1, 12000+1):
    for num in range(int(np.ceil(denom/3)), int(np.ceil(denom/2))):
        if gcd(num, denom) == 1:
            s += 1
print s-1
