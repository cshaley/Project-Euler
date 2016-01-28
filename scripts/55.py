#Euler Problem #55
def ispalindrome(x):
    return str(x)==str(x)[::-1]

def lychrel(x,ct=0):
    x = x + int(str(x)[::-1])
    ct+=1
    if ispalindrome(x):
        return False
    if ct>50:
        return True
    return lychrel(x,ct)
ls=[]
for i in range(1,10001):
    if lychrel(i):
        ls.append(i)
print len(ls)