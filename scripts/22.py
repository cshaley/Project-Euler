#Euler Project #22
def wordtosum(word):
    return sum([ord(char)-64 for char in word])

x = pd.read_csv('../resources/names.txt')
x = x[sorted(x.columns.values)]
y=[]
for ix,word in enumerate(x.columns.values):
    y.append((ix+1)*wordtosum(word))
print sum(y)