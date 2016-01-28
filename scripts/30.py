#Euler Project #30
print sum([i for i in range(2,200000) if sum([int(j)**5 for j in str(i)])==i])