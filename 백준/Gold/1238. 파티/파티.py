N, M, X=map(int, input().split())
Ti=[[9999999]*N for i in range(N)]
for i in range(M):
  start, end, time=map(int, input().split())
  Ti[start-1][end-1]=time
for i in range(N):
  Ti[i][i]=0
list_least=[]
for i in range(2):
  least=[9999999]*N
  least[X-1]=0
  visited=[]
  a=X-1
  while len(visited)<N:
    visited.append(a)
    for idx, i in enumerate(Ti[a]):
      least[idx]=min(least[idx], least[a]+i)
    mn=[]
    for idx, i in enumerate(least):
      if idx not in visited:
        mn.append([i, idx])
    if not mn:
      break
    a=min(mn, key=lambda x:x[0])[1]
  list_least.append(least)
  Ti=list(zip(*Ti))
sm=[]
for i in zip(*list_least):
  if sum(i)<9999999:
    sm.append(sum(i))
  
print(max(sm))