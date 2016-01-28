#Euler Problem #92
def getsto89(num):
    count = 0
    while(True):
        num = sum([int(y)**2 for y in str(num)])
        if num == 89:
            return 1
        elif num == 1:
            return 0
        count += 1
        if count > 200:
            return -1
start_time =time.time()
arr={}
for i in range(1,10000000):
    x = sum([int(y)**2 for y in str(i)])
    try:
        arr[i] = arr[x]
    except:
        arr[i] = getsto89(x)
print sum(arr.values())