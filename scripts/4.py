#Euler Project #4
def ispalindrome(x):
    return str(x)==str(x)[::-1]
print [i*j for i in range(1,1000) for j in range(1,i+1) if ispalindrome(i*j)][-1]