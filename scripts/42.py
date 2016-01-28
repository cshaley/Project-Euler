#Euler Problem 42
x=''
with open('../resources/words.txt','r') as f:
    x=f.read().replace('"','').replace('\n','').split(',')
for ix, entry in enumerate(x):
    entry=entry.lower()
    a=[]
    for char in entry:
        a.append(ord(char)-96)
    x[ix]=sum(a)
tris = [.5*n*(n+1) for n in range(1,30)]
out = [a for a in x if a in tris]
print len(out)