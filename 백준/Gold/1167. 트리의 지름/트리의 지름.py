from collections import deque

V=int(input())
tree=[[] for i in range(V)]
for i in range(V):
    node, *cost=map(int, input().split())
    j=0
    while True:
        if cost[j]!=-1:
            tree[node-1].append((cost[j], cost[j+1]))
            j+=2
        else:
            break
b=0
for j in range(2):
    queue = deque([b])
    visited=[0]*V
    visited[b]=1
    while queue:
        a=queue.popleft()
        for i, c in tree[a]:
            if not visited[i-1]:
                queue.append(i-1)
                visited[i-1]=visited[a]+c
    b=visited.index(max(visited))
print(visited[b]-1)