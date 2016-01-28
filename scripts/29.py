#Euler Project #29
l=[0]*(99*99)
for a in range(2,101):
    for b in range(2,101):
        l[(a-2)*99+b-2]=a**b
print len(set(l))