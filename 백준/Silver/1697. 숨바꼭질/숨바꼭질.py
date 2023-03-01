from collections import deque

N, K=map(int, input().split())
queue=deque([N])
visited=[9999999]*100001
visited[N]=0
for_break=False
if K==N:
    print(0)
    queue.pop()
while queue:
    a=queue.popleft()
    for i in [a-1, a+1, 2*a]:
        if i==K:
            for_break=True
            print(visited[a]+1)
            break
        if  0<=i<=100000 and visited[i]==9999999:
            queue.append(i)
            visited[i]=visited[a]+1
    if for_break:
        break