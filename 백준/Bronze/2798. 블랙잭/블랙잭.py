from itertools import combinations

N, M=map(int, input().split())
card=list(map(int, input().split()))
sm=[]
for i in list(combinations(card, 3)):
    if sum(i)<=M:
        sm.append(sum(i))
print(max(sm))