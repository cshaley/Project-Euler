#Euler Project #99
import math
max = 0
maxidx = 0
with open('../resources/base_exp.txt','r') as f:
    for ix,line in enumerate(f):
        line=line.replace('\n','').split(',')
        if int(line[1])*math.log(int(line[0]))> max:
            max = int(line[1])*math.log(int(line[0]))
            maxidx = ix+1
print maxidx