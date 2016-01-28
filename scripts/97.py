#Euler Project 97
n=1
for i in range(7830457):
   n = (2*n) %10000000000
n*=28433
n+=1
n%=10000000000
print n