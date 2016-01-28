#Euler Project #25
x=[1,1,2]
count=3
while(True):
    count+=1
    x.pop(0)
    x.append(sum(x))
    if x[2] > 10**999:
        break
print count