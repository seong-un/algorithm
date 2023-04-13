from itertools import combinations

N, M=map(int, input().split())
lst=[i for i in range(1, N+1)]
nCm=list(combinations(lst, M))
for i in nCm:
    print(*i)