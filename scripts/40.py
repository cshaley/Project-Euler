#Euler Problem 40
y=''
for x in range(1000000):
    y+=str(x)
s=[]
for x in range(7):
   s.append(int(y[10**x]))
print s
print 15*14