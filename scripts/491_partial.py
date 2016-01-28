#Euler Project #491
def isdoublepandigital(x):
    x=str(x)
    nums = ['1','2','3','4','5','6','7','8','9','0']
    for num in nums:
        if x.count(num) != 2:
            return False
    return True
#isdoublepandigital(40561817073823564929)
import math
import itertools
#I don't think this is how you solve this
# I think you get how many double pandigital numbers there are
x = (math.factorial(20)/2**10) * 18/20 /11
print "Good general approximation: " + "{:,}".format(x)
#y = [int(''.join(a)) for a in itertools.permutations(['0','1','2','3','4','5','6','7','8','9',\
#        '0','1','2','3','4','5','6','7','8','9'],10) if a[0]!='0' and int(''.join(a))%11==0]
#print "Actual number: " + "{:,}".format(len(set(y)))
print "this will take fiveever"