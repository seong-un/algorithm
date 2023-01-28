import sys
sys.setrecursionlimit(1000000)
T=int(input())

for _ in range(T):
  N, M, K=map(int, input().split())
  graph=[[0]*M for _ in range(N)]
  for _ in range(K):
    start, end = map(int,input().split())
    graph[start][end] = 1
  
  def dfs(n,m):
    graph[n][m]=0
    if n<N-1:
      if graph[n+1][m]==1:
        graph[n+1][m]=0
        dfs(n+1,m)
    if n>0:
      if graph[n-1][m]==1:
        graph[n-1][m]=0
        dfs(n-1,m)
    if m>0:
      if graph[n][m-1]==1:
        graph[n][m-1]=0
        dfs(n,m-1)
    if m<M-1:
      if graph[n][m+1]==1:
        graph[n][m+1]=0
        dfs(n,m+1)
  
  ji=0
  for i in range(N):
    for j in range(M):
      if graph[i][j]==1:
        ji+=1
        dfs(i,j)
  
  print(ji)