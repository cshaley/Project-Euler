#Euler Project Problem #493
import math, random
balls = [[i]*10 for i in range(1,8)]
balls = [item for sublist in balls for item in sublist]
def choose20(b):
    c = b[:]
    d = []
    for i in range(20):
        d.append(c.pop(random.randint(0,len(c)-1)))
    return len(set(d))
s = 0
numit=100000
for i in range(numit):
    s += choose20(balls)
print 'Simulated expected value (approx): ' + str(s*1./numit*1.)

def nCr(n,r):
    f = math.factorial
    return f(n)*1. / f(r) / f(n-r)

#p(not getting a color in 20 draws) = 60/70*59/69*...40/50
f = math.factorial
pn = (f(60)*1./f(39)) / (f(70)*1./f(49))
pg = 1 - pn
print "Calculated expected value: " + str(pg*7)

print 'Expected value 1 draw: ' + str(1)
#ex(2) = 1 + (1-p(same)) = 
print 'Expected value 2 draws: ' + str(2-9./69.)
#ex(3) = 1 + 


#AHA! 
# 7*(1-number of ways to avoid picking a color/#ways to pick 20 from 70)
# 7*(1-60 choose 20/70 choose 20)
print 'Expected value 20 draws: ' + str(7*(1-nCr(60,20)/nCr(70,20)))