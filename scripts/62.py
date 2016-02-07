#Euler Project #62
#This could certainly be a lot faster.  Takes like 5 seconds or so.
cubes = [a**3 for a in range(1,10**6)]
d = {}

for a in cubes:
    d[''.join(sorted(str(a)))] = ''
    
for ix, cube in enumerate(cubes):
    if len(d[''.join(sorted(str(cube)))]) > 0:
        d[''.join(sorted(str(cube)))] = d[''.join(sorted(str(cube)))]+','+str(ix+1)
    else:
        d[''.join(sorted(str(cube)))] = str(ix+1)

min1 = 9999
minitem = []
for item in d.values():
    if len(item.split(',')) == 5:
        min2 = min(item.split(','))
        if int(min2) < min1:
            min1 = int(min2)
            minitem = item
print min1
print minitem
print min1**3
