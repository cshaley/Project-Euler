#Euler Project #125
#Get a list of all palindromes less than 10**8
#Check if each one can be created by sum of consecutive squares
#
# OR
#
#Create each sum of consecutive squares under 10**8
#Check if each one is a palindrome
#
#I think the second solution is much faster.
def ispalindrome(x):
    return str(x)==str(x)[::-1]
maxnum = 10**8
pals = set()
for i in range(2, int(maxnum**0.5)):
    for j in range(1,i+1):
        x = range(i-j+1,i+1)
        if len(x)>1:
            x = sum(a*a for a in x)
            if x > maxnum:
                break
            if ispalindrome(x):
                #print x
                #print range(i-j+1,i+1)
                pals.add(x)
#    if i%100 == 0:
#        print i
print sum(pals)
