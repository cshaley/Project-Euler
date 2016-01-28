#Euler Project #28
#21 22 23 24 25
#20  7  8  9 10
#19  6  1  2 11
#18  5  4  3 12
#17 16 15 14 13

#1 9 25 49 81 121 ...
#1 3 13 25+(7-1) 49+(9-1)... 
#1 5 17 31+(7-1) 37+(9-1)...
#1 7 21 37+(7-1) 43+(9-1)...

def spiralsum(size):
    squares = [a**2 for a in range(1,size+1,2)]
    lr=[]
    for ix, a in enumerate(squares):
        lr.append(a+((ix+1)*2))
    lr.pop(-1)
    ll=[]
    for ix, a in enumerate(squares):
        ll.append(a+((ix+1)*4))
    ll.pop(-1)
    ul=[]
    for ix, a in enumerate(squares):
        ul.append(a+((ix+1)*6))
    ul.pop(-1)
    return sum(squares+lr+ll+ul)
print spiralsum(1001)