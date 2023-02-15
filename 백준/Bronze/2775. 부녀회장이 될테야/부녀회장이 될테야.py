T=int(input())
for _ in range(T):
    k=int(input())
    n=int(input())
    house=[0]*n
    for i in range(n):
        house[i] = i + 1
    while k>0:
        upper = [0] * n
        for i in range(n):
            upper[i]=sum(house[:i+1])
        house=upper[:]
        k-=1
    print(upper[-1])