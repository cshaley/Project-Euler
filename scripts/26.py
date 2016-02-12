oast login: Sun Feb  7 17:42:32 2016 from fe
La#26
ds = range(999,0,-1)

def findlen(x):
    s = set()
    n = 1
    while True:
        if x < n:
            q = int(n/x)
            n = n%x
            if n == 0:
                return len(s)+1
            if n not in s:
                s.add(n)
            else:
                return len(s)
        elif x == n:
            return len(s)+1
        elif x>n:
             n *= 10

maxdlen = 0
maxd = 0
for d in ds:
    if maxdlen > d:
        break
    l = findlen(d)
    if l > maxdlen:
        maxdlen = l
        maxd = d
print maxdlen # Maybe this should be higher?
print maxd  login: Sun Feb  7 17:42:32 2016 from fe
