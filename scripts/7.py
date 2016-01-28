#Euler Project #7
def isprime(x):
    for n in range(3,int(x/2.)+1,2):
        if x%n==0:
            return False
    return True
it=3
primecount=3
highprime = 0
while primecount<10001:
    it+=1
    if isprime(it):
        highprime=it
        primecount+=1
print highprime