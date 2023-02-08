import itertools

dwarf=[0]*9
for i in range(9):
    dwarf[i]=int(input())
nCr=itertools.combinations(dwarf, 7)
for i in list(nCr):
    if sum(i)==100:
        dwarf=list(i)
        dwarf.sort()
        break
for i in dwarf:
    print(i)