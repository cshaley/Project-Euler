#Euler Project #2
x=[1,1,2]
sum1=2
while x[2]<4000000:
    x.pop(0)
    x.append(sum(x))
    if x[2]%2==0:
        sum1+=x[2]
print sum1
