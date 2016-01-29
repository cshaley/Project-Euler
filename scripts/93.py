#Euler Project #93
import itertools
from __future__ import division

ops = ['+','-','/','*']
pars = ['(',')']

op_combos = list(itertools.combinations_with_replacement(ops,3))
op_combos = [x for a in op_combos for x in list(itertools.permutations(a,3))]
singleparlocs=[(0, 3), (0, 5), (2, 5), (2, 7), (4, 7)]
doubleparlocs = [((0,'('), (0,'('), (3,')'), (5,')')), \
                 ((0,'('), (3,')'), (4,'('), (7,')')), \
                 ((2,'('), (2,'('), (5,')'), (7,')'))]

compareset = set(range(1,100))
totalnums = ['1','2','3','4','5','6','7','8','9']
numlists = list(itertools.combinations(totalnums,4))
dictout = {}

for nums in numlists:
    num_combos = list(itertools.permutations(nums,4))
    x=set()
    for op in op_combos:
        for numset in num_combos:
            st = numset[0]
            for i in range(3):
                st += op[i]+numset[i+1]
            for a in singleparlocs:
                stn = st[:a[0]]+'('+st[a[0]:a[1]]+')'+st[a[1]:]
                try:
                    x.add(abs(eval(stn)))
                    #print stn + ' = ' + str(eval(stn))
                except:
                    pass
            for a in doubleparlocs:
                stn = st[:a[0][0]]+a[0][1]+st[a[0][0]:a[1][0]]+a[1][1]+st[a[1][0]:a[2][0]]+a[2][1]+\
                        st[a[2][0]:a[3][0]]+a[3][1]+st[a[3][0]:]
                try:
                    x.add(abs(eval(stn)))
                    #print stn + ' = ' + str(eval(stn))
                except:
                    pass
            try:
                x.add(abs(eval(st)))
                #print st + ' = ' + str(eval(st))
            except:
                pass
    dictout[''.join(nums)] = min(compareset-x)

print max(dictout, key=dictout.get)
