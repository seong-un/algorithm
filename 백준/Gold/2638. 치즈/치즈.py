from collections import deque

N, M=map(int, input().split())
cheese=[[] for i in range(N)]
for i in range(N):
    cheese[i]=list(map(int, input().split()))
loop=True
time=0
while loop:
    cheese[0][0]=2
    queue=deque()
    queue.append((0,0))
    dx=[-1, 1, 0, 0]
    dy=[0, 0, -1, 1]
    while queue:
        x,y=queue.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if nx<0 or ny<0 or nx>N-1 or ny>M-1 or cheese[nx][ny]:
                continue
            queue.append((nx, ny))
            cheese[nx][ny]=2
    for i in range(N):
        for j in range(M):
            cnt=0
            if cheese[i][j]==1:
                for k in range(4):
                    nx=i+dx[k]
                    ny=j+dy[k]
                    if cheese[nx][ny]==2:
                        cnt+=1
                    if cnt>=2:
                        cheese[i][j]=0
                        break
    loop=False
    for i in range(N):
        for j in range(M):
            if cheese[i][j]==2:
                cheese[i][j]=0
            if cheese[i][j]==1:
                loop=True
    time+=1
print(time)