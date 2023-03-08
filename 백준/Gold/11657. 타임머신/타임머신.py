N, M=map(int, input().split())
route=[[] for i in range(M)]
for m in range(M):
  route[m]=list(map(int, input().split()))
least=[999999999]*N
least[0]=0

def Bellman_Ford():
  for n in range(N):
    for m in route:
      start=m[0]-1
      end=m[1]-1
      cost=m[2]
      if least[start]!=999999999 and least[end]>least[start]+cost:
        least[end]=least[start]+cost
        if n==N-1:
          return []
  return least

least=Bellman_Ford()
if least:
  for i in least[1:]:
    if i==999999999:
      print(-1)
    else:
      print(i)
else:
  print(-1)