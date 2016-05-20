import itertools

with open('../resources/p059_cipher.txt','r') as f:
    txt = f.read()
lst = txt.strip().split(',')
lst = [int(a) for a in lst]

def decode(password, l):
    out = []
    pwlen = len(password)
    for ix, item in enumerate(l):
        out.append(item^ord(password[ix%pwlen]))
    return ''.join(chr(i) for i in out)

def check_english(s):
    s = s.lower()
    if "the" in s and "that" in s:
        return True

for combo in itertools.permutations('abcdefghijklmnopqrstuvwxyz',3):
    pw = ''.join(combo)
    t = decode(pw, lst)
    if check_english(t):
        print pw
        print t
        print sum(ord(i) for i in t)
        break
