from collections import deque

N, M=map(int, input().split())
route=[[0]*N for i in range(N)]
for i in range(M):
  u, v=map(int, input().split())
  route[u-1][v-1]=1
  route[v-1][u-1]=1
queue=deque([0])
visited=[False]*N
visited[0]=True
element=1
while True:
  while queue:
    a=queue.popleft()
    
    for idx, i in enumerate(route[a]):
      if i and not visited[idx]:
        visited[idx]=True
        queue.append(idx)
  if False in visited:
    queue.append(visited.index(False))
    visited[visited.index(False)]=True
    element+=1
  else:
    break
print(element)