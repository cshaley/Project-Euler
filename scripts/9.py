#Euler Project #9
print [a*b*c for c in range(1,999) for b in range(1,c) for a in range(1,b) if a+b+c==1000 and a<b and b<c and a**2+b**2==c**2][0]