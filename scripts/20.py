#Euler Project 20
p=1
for i in range(1,101):
    p=p*i
print sum([int(x) for x in str(p)])