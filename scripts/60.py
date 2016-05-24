import itertools
import time
from utils import primesfrom2to

t = time.time()

# Settings for Problem #60
maxprime = 10**4  # Max prime to consider for the list
maxsetlen = 5  # Set length to find


# Function to check for the condition needed in problem 60 ( for two items )
def cpc(a, b):
    return concatenatable_primes_check(a, b)


def concatenatable_primes_check(a, b):
    return int(str(a) + str(b)) in pdict and int(str(b) + str(a)) in pdict


# Prime number dictionaries (for O(1) prime checks)
babypdict = {p: 1 for p in primesfrom2to(maxprime)}
pdict = {p: 1 for p in primesfrom2to(maxprime**2)}

# All possible 2 member combinations of primes below maxprime
combos = itertools.combinations(babypdict.keys(), 2)
successful_combos = []

# Remove non cpc compliant prime number combinations
for combo in combos:
    a = combo[0]
    b = combo[1]
    if cpc(a, b):
        successful_combos.append((a, b))

# Create a dictionary of primes referring to the other primes they map to
suc_nums_d = {}
for ix, combo in enumerate(successful_combos):
    a = combo[0]
    b = combo[1]
    if a in suc_nums_d:
        suc_nums_d[a].update([b])
    else:
        suc_nums_d[a] = set([b])
    if b in suc_nums_d:
        suc_nums_d[b].update([a])
    else:
        suc_nums_d[b] = set([a])

# Find primes that map to the same things and make a list of them
suc_isect = []
for ix, num in enumerate(suc_nums_d.keys()):
    for num2 in suc_nums_d.keys()[ix+1:]:
        isect = suc_nums_d[num].intersection(suc_nums_d[num2])
        if len(isect) >= maxsetlen-2 and num in suc_nums_d[num2] \
           and num2 in suc_nums_d[num]:
            suc_isect.append((num, num2, isect))

# Find full sets of primes that map to each other
iset = []
for a, b, cset in suc_isect:
    cset.update([a, b])
    for num in cset:
        if num in [a, b]:
            pass
        else:
            is1 = suc_nums_d[num].intersection(cset)
            if len(is1) >= maxsetlen-1:
                iset += (is1, )

# Remove duplicate sets, remove sets that don't fully meet the criteria
osets = set([])
for ix, s in enumerate(iset):
    for a in iset[ix+1:]:
        b = s.union(a)
        if len(b) == maxsetlen:
            failflag = 0
            for combo in itertools.permutations(b):
                z = combo[0]
                x = combo[1]
                if not cpc(z, x):
                    failflag = 1
                    break
            if not failflag:
                osets.update((tuple(sorted(b)), ))

# Find minimum sum of a set and print that minimum sum and that prime set
minsum = 10**8
for tup in osets:
    s = sum(tup)
    if s < minsum:
        minsum = s
        mintup = tup

print mintup
print minsum
print "Took {} seconds".format(time.time() - t)
