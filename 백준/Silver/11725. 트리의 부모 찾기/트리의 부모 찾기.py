import sys
input=sys.stdin.readline
from collections import deque

N=int(input())
tree=[[] for i in range(N+1)]
for i in range(N-1):
    a,b=map(int, input().split())
    tree[a].append(b)
    tree[b].append(a)

queue=deque([1])
parent=[0]*(N+1)
for _ in range(N):
    a=queue.popleft()
    for i in tree[a]:
        if not parent[i]:
            parent[i]=a
            queue.append(i)
for i in parent[2:]:
    print(i)