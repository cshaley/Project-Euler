#Euler Project #34
import math
print sum([x for x in range(10,1000000) if sum([math.factorial(int(y)) for y in str(x)])==x])