#Euler Project #33
def iscurious(x,y):
    if int(str(y)[1]) != 0 and int(str(x)[0]) != int(str(x)[1]) and int(str(x)[1]) == int(str(y)[0]):
        return int(str(x)[0])*1. / int(str(y)[1]) == x*1. / y
    return False
fracs = [[x,y] for x in range(10,100) for y in range(10,100) if iscurious(x,y)]
p = [1,1]
for value in fracs:
    p[0]*=value[0]
    p[1]*=value[1]
p=p[0]*1./p[1]
p
print int(1/p)