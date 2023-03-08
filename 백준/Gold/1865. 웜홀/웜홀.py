import sys
input=sys.stdin.readline

def Bellman_Ford(start, N):
  global result
  least[start]=0
  for n in range(N):
    for r in route:
      current=least[r[0]-1]
      future=least[r[1]-1]
      cost=r[2]
      if current!=999999999 and future>current+cost:
        least[r[1]-1]=current+cost
        if n==N-1:
          result=1
  return least
          
for _ in range(int(input())):
    N, M, W = map(int, input().split())
    route = [() for i in range(2*M+W)]
    for m in range(M):
        S, E, T = map(int, input().split())
        route[2*m]=(S, E, T)
        route[2*m+1]=(E, S, T)
    for w in range(W):
        S, E, T = map(int, input().split())
        route[2*M+w]=(S, E, -T)
    result=0
    start=0
    least=[999999999]*N
    while 999999999 in least:
      least=Bellman_Ford(start, N)
      for idx, i in enumerate(least):
        if i==999999999:
          start=idx
    if result==0:
      print("NO")
    else:
      print("YES")