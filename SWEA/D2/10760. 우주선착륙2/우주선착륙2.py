T=int(input())
for test_case in range(1, T+1):
  N, M=map(int, input().split())
  Aij=[0]*N
  for i in range(N):
    Aij[i]=list(map(int, input().split()))
  dx=[-1, 1, 0, 0, -1, 1, -1, 1]
  dy=[0, 0, -1, 1, -1, 1, 1, -1]
  picture=0
  for i in range(N):
    for j in range(M):
      sm=0
      for k in range(8):
        nx=i+dx[k]
        ny=j+dy[k]
        if nx<0 or ny<0 or nx>N-1 or ny>M-1:
          continue
        if Aij[i][j]>Aij[nx][ny]:
          sm+=1
      if sm>=4:
        picture+=1
  print(f'#{test_case} {picture}')