from collections import deque

N, M, V=map(int, input().split())
route=[[0]*N for i in range(N)]
for i in range(M):
    a,b=map(int, input().split())
    route[a-1][b-1]=1
    route[b-1][a-1]=1
queue=deque([V-1])
visited=[False]*N
DFS=[]
while queue:
    a=queue.pop()
    if not visited[a]:
        DFS.append(a+1)
    visited[a]=True
    for idx in range(N-1, -1, -1):
        if route[a][idx]==1 and not visited[idx]:
            queue.append(idx)
print(*DFS)

BFS=[]
queue=deque([V-1])
visited=[False]*N
BFS=[]
while queue:
    a=queue.popleft()
    if not visited[a]:
        BFS.append(a+1)
    visited[a]=True
    for idx in range(N):
        if route[a][idx]==1 and not visited[idx]:
            queue.append(idx)
print(*BFS)