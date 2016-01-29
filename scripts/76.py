#Euler Problem #76
#This is just problem 31 but rephrased
#99:1:1
#98:2:2,1+1
#97:3:3,2+1,1+1+1
#96:5:4,3+1,2+2,2+1+1,1+1+1+1
#95:7:5,(all of 96 ways +1),3+2
#94:11:6,(all of 95 ways +1), 3+3, 4+2, 2+2+2
#93:15:7,(all of 94 ways +1), 3+4, 5+2, 2+3+2
#92:22:8,(all of 93 ways +1), 4+4, 2+2+2+2, 5+3, 4+2+2, 3+3+2, 6+2
target = 100
coins = range(1,100)
ways = [0]*101
ways[0] = 1

for i in coins:
    for j in range(i,target+1):
        ways[j] += ways[j-i]
print ways
