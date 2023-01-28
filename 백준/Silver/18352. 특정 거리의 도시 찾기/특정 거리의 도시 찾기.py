import sys
input = sys.stdin.readline

N, M, K, X=map(int, input().split())
route=[]
for i in range(M):
  route.append(list(map(int, input().split())))

visiting=[]
vst=[X]
least=["Inf"]*N
least[X-1]=0
mini=0
visited={X}
for _ in range(N):
  mini+=1
  for j in vst:
    for i in range(len(route)):
      if route[i][0]==j and route[i][1] not in visited:
        visiting.append(route[i][1])
        least[route[i][1]-1]=mini
        visited.add(route[i][1])
  vst=visiting
  if mini==K:
    break
  else:
    visiting=[]

printing=[]
for i in range(len(least)):
  if least[i]==K:
    printing.append(i+1)
if not printing:
  print(-1)
else:
  for i in range(len(printing)):
    print(printing[i])