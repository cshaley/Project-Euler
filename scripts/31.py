#Euler Project #31
#I copied this because I was curious as to how to solve this - it is a very genius design.  
target = 200
coins = [1,2,5,10,20,50,100,200]
ways = [0]*201
ways[0] = 1

for i in coins:
    for j in range(i,target+1):
        ways[j] += ways[j-i]
print ways