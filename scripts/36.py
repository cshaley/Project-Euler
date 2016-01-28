#Euler Project #36
def ispalindrome(x):
    return str(x)==str(x)[::-1]
print sum([x for x in range(1000000) if ispalindrome(x) and ispalindrome(int("{0:b}".format(x)))])