import sys
input=sys.stdin.readline

M, N, H=map(int, input().split())
tomato=[]
for j in range(H):
    tomato.append([list(map(int, input().split())) for i in range(N)])
dx=[1, -1, 0, 0, 0, 0]
dy=[0, 0, 1, -1, 0, 0]
dz=[0, 0, 0, 0, 1, -1]

spread=set()
for i in range(N):
    for j in range(M):
        for h in range(H):
            if tomato[h][i][j]==1:
                spread.add((h,i,j))

day=0
while True:
    spread2=spread
    spread=set()
    for h, i, j in spread2:
        for k in range(6):
            nx=i+dx[k]
            ny=j+dy[k]
            nz=h+dz[k]
            if nx<0 or ny<0 or nz<0 or nx>N-1 or ny>M-1 or nz>H-1 or tomato[nz][nx][ny]:
                continue
            spread.add((nz, nx, ny))
    if not spread:
        break
    for h, i, j in spread:
        tomato[h][i][j]=1
    day+=1

minus=False
for i in tomato:
    for j in i:
        if 0 in j:
            minus=True
            break

if minus:
    print(-1)
else:
    print(day)