N, M=map(int, input().split())
maze=[]
for i in range(N):
  char=[]
  for i in input():
    char.append(int(i))
  maze.append(char)

def mazesolution(i,j):
  if i!=N-1:
    if maze[i+1][j]==1:
      maze[i+1][j]+=maze[i][j]
      bfs.append([i+1,j])
  if i!=0:
    if maze[i-1][j]==1:
      maze[i-1][j]+=maze[i][j]
      bfs.append([i-1,j])
  if j!=M-1:
    if maze[i][j+1]==1:
      maze[i][j+1]+=maze[i][j]
      bfs.append([i,j+1])
  if j!=0:
    if maze[i][j-1]==1:
      maze[i][j-1]+=maze[i][j]
      bfs.append([i,j-1])
  return bfs

bfs=[[0,0]]
while [N-1, M-1] not in bfs:
  bfss=bfs
  bfs=[]
  for i in range(len(bfss)):
    mazesolution(bfss[i][0], bfss[i][1])

print(maze[N-1][M-1])