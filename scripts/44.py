#Euler Project #44
num=10**4
pents={}
for i in range(1,num):
    pents[(i)*(3*(i)-1)/2]=1
keys=pents.keys()
sps=[]
for i in range(num):
    for j in range(i+1,num):
        try:
            if pents[keys[i]+keys[j]] and pents[abs(keys[j]-keys[i])]:
                sps.append((keys[i],keys[j]))
        except:
            pass
print sps
print abs(sps[0][0]-sps[0][1])