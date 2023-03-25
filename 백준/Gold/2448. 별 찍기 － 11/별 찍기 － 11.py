import math

N=int(input())
star=['*', '* *', '*****']
k=round(math.log2(N/3))
S=1
stars=star[:]
while S<=k:
    for idx, i in enumerate(star):
        stars.append(i+' '*(3*2**S-1-idx*2)+i)
    S+=1
    star=stars[:]

for idx, i in enumerate(stars):
    print(' '*(N-idx-1)+i+' '*(N-idx-1))