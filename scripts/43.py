#Euler Problem 43
def ispandigital(x):
    nums = ['1','2','3','4','5','6','7','8','9','0']
    for num in nums:
        if num not in x:
            return False
    return True

def hasprimeperty(x):
    x=str(x)
    if int(x[3])%2==0 and int(x[2:4])%3==0 and int(x[5])%5==0 and int(x[4:7])%7==0 and int(x[5:8])%11==0 \
        and int(x[6:9])%13==0 and int(x[7:])%17==0:
            return True
    return False
import itertools
y = list(itertools.permutations(['1','2','3','4','5','6','7','8','9','0'],10))
y = [''.join(a) for a in y if a[0]!='0']
y = [int(a) for a in y if hasprimeperty(a)]
print y
print sum(y)