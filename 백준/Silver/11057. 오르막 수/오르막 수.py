import copy

N=int(input())
sm=[1,1,1,1,1,1,1,1,1,1]
hap=[1,1,1,1,1,1,1,1,1,1]
for j in range(N-1):
    hap=[sum(sm)]
    for i in range(10):
        hap.append(hap[-1]-sm[i])
    sm=copy.deepcopy(hap)
print(sum(hap)%10007)