#Euler Project #38
def ispandigital(x):
    nums = ['1','2','3','4','5','6','7','8','9']
    for num in nums:
        if num not in x:
            return False
    return True

max = 0
for i in range(10,10000):
    x=[]
    for j in range(1,6):
        x.append(i*j)
        s = ''.join([str(y) for y in x])
        if len(s) == 9:
            if not ispandigital(s):
                break
            if int(s)>max:
                max = int(s)
            break
        elif len(s) > 9:
            break
print max