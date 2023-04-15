import math

M, N=map(int, input().split())
prime=[i for i in range(N+1)]
prime[1]=0
for i in range(N+1):
    for j in range(i**2, N+1):
        if prime[i] == 0:
            break
        if prime[j]==0:
            continue
        if prime[j]%prime[i]==0:
            prime[j]=0
for i in prime[M:]:
    if i==0:
        continue
    print(i)