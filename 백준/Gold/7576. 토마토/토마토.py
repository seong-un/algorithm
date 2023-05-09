import sys
input=sys.stdin.readline

M, N=map(int, input().split())
tomato=[list(map(int, input().split())) for i in range(N)]
dx=[1, -1, 0, 0]
dy=[0, 0, 1, -1]

spread=set()
for i in range(N):
    for j in range(M):
        if tomato[i][j]==1:
            spread.add((i,j))

day=0
while True:
    spread2=spread
    spread=set()
    for i, j in spread2:
        for k in range(4):
            nx=i+dx[k]
            ny=j+dy[k]
            if nx<0 or ny<0 or nx>N-1 or ny>M-1 or tomato[nx][ny]:
                continue
            spread.add((nx, ny))
    if not spread:
        break
    for i, j in spread:
        tomato[i][j]=1
    day+=1

minus=False
for i in tomato:
    if 0 in i:
        minus=True
        break

if minus:
    print(-1)
else:
    print(day)