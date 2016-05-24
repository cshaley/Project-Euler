import numpy as np
import itertools as itls

def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in xrange(int(n**0.5)/3+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

ps = primesfrom2to(10**8)
ps = ps[4:]
pdict = {p:None for p in ps}



def check_for_pattern(p, pdict, target):
    cnt = 0
    s = str(p)
    l = len(s)
    permutation_list = []
    for i in range(l-1):
        permutation_list.append(itls.combinations(range(l), i+1))
    replacement_loc_list = itls.chain.from_iterable(permutation_list)


    locs_replaced = None

    for rlocs in replacement_loc_list:
        replace_p_cnt = 0
        pls = []
        for i in range(10):
            ril = replace_in_locs(p, i, rlocs)
            if len(str(ril)) == l:
                if ril in pdict:
                    locs_replaced = rlocs
                    pls.append(ril)
                    replace_p_cnt += 1
                if replace_p_cnt == target:
                    return pls, locs_replaced
    return None, None

def replace_in_locs(prime, num, locs):
    s = list(str(prime))
    for loc in locs:
        s[loc] = str(num)
    return int(''.join(s))

for p in ps:
    x, y = check_for_pattern(p, pdict, 8)
    if x or y:
        break

print x
print y



