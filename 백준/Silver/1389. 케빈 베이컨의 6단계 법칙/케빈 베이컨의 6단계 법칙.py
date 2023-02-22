from collections import deque

N, M = map(int, input().split())
friends = [[0] * N for i in range(N)]
for i in range(M):
    a, b = map(int, input().split())
    friends[a - 1][b - 1] = 1
    friends[b - 1][a - 1] = 1
bacon = [0]*N
for v in range(N):
    if 1 not in friends[v]:
        continue
    cnt = [0]*N
    cnt[v]=1
    queue = deque([v])
    while queue:
        a=queue.popleft()
        for idx, i in enumerate(friends[a]):
            if i==1 and not cnt[idx]:
                queue.append(idx)
                cnt[idx]=cnt[a]+1
    bacon[v]=sum(cnt)-N
mn=[]
for idx, i in enumerate(bacon):
    if i!=0:
        mn.append((idx, i))
print(min(mn, key=lambda x:x[1])[0]+1)