from collections import deque

N, M=map(int, input().split())
Tn, *know=map(int, input().split())
route=[[0]*N for i in range(N)]
party=[0]*M
for i in range(M):
    n, *tup=map(int, input().split())
    party[i]=list(tup)
    for j in tup:
        for k in tup:
            route[j-1][k-1]=1
queue=deque(know)
visited=set()
zero=False
if not queue:
    zero=True
    print(M)
while queue:
    a=queue.popleft()
    visited.add(a)
    for idx, i in enumerate(route[a-1]):
        if i and idx+1 not in visited:
            queue.append(idx+1)
for i in party:
    for j in i:
        if j in visited:
            M-=1
            break
if not zero:
    print(M)