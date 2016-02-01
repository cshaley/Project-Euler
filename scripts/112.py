#Euler Project #112
def isbouncy(x):
    x=str(x)
    y = ''
    for ix in range(len(x)-1):
        if x[ix]<x[ix+1]:
            y+='i'
        if x[ix]>x[ix+1]:
            y+='d'
    if 'i' in y and 'd' in y:
        return True
    return False

i = 0
bct = 0
while True:
    i+=1
    if isbouncy(i):
        bct+=1
    if bct*1./i == 0.99:
        print i
        break
