from collections import deque

n=int(input())
tree=[]
for i in range(n-1):
    s, e, c=list(map(int, input().split()))
    tree.extend([[s,e,c], [e,s,c]])

queue=deque([0])
for j in range(2):
    visited=['0']*n
    visited[queue[0]]=0
    while queue:
        a=queue.popleft()
        for i in tree:
            if i[0]-1==a and visited[i[1]-1]=='0':
                visited[i[1]-1]=visited[a]+i[2]
                queue.append(i[1]-1)
    queue.append(visited.index(max(visited)))
print(max(visited))