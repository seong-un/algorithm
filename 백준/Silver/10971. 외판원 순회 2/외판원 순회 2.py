from itertools import permutations
import sys
input=sys.stdin.readline

N=int(input())
costs=[list(map(int, input().split())) for i in range(N)]
turns=[i for i in range(N)]
min_cost=int(1e9)
for turn in list(permutations(turns, N)):
    cost=0
    for i in range(N-1):
        c=costs[turn[i]][turn[i+1]]
        for_break=False
        if not c:
            for_break=True
            break
        cost+=c
    if for_break:
        continue
    c=costs[turn[-1]][turn[0]]
    if not c:
        continue
    cost+=c
    min_cost=min(min_cost, cost)
print(min_cost)