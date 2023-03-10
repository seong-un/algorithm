from collections import deque

N, M=map(int, input().split())
maze=[[] for i in range(N)]
for i in range(N):
  maze[i]=list(input())
maze[0][0]=1

queue=deque()
queue.append((0,0,0))
dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]
visited=[[['0']*2 for i in range(M)] for j in range(N)]
visited[0][0][0]=1
while queue:
  a=queue.popleft()
  for i in range(4):
    power=a[2]
    nx=a[0]+dx[i]
    ny=a[1]+dy[i]
    if nx<0 or ny<0 or nx>N-1 or ny>M-1 or visited[nx][ny][a[2]]!='0':
      continue
    if maze[nx][ny]=='1':
      if a[2]==1:
        continue
      else:
        power=1
    if maze[nx][ny] in ['0', '1']:
      visited[nx][ny][power]=visited[a[0]][a[1]][a[2]]+1
      queue.append((nx, ny, power))
    if nx==N-1 and ny==M-1:
      break
if visited[-1][-1]==['0', '0']:
  print(-1)
elif visited[-1][-1][0]=='0' and visited[-1][-1][1]!='0':
  print(visited[-1][-1][1])
elif visited[-1][-1][0]!='0' and visited[-1][-1][1]=='0':
  print(visited[-1][-1][0])
else:
  print(min(visited[-1][-1]))