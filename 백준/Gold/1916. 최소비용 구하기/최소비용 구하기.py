N=int(input())
M=int(input())
bus=[[999999999]*N for i in range(N)]
for i in range(M):
    s, e, c=map(int, input().split())
    bus[s-1][e-1]=min(c, bus[s-1][e-1])
start, end=map(int, input().split())
least=[999999999]*N
least[start-1]=0
visited=[False]*N
if start==end:
  print(0)
else:
  while True:
      visited[start-1]=True
      for idx, i in enumerate(bus[start-1]):
          if not visited[idx] and least[idx]>least[start-1]+bus[start-1][idx]:
              least[idx]=least[start-1]+i
      mn=[]
      for idx, i in enumerate(least):
        if visited[idx]:continue
        mn.append((idx, i))
      start=min(mn, key=lambda x:x[1])[0]+1
      if start==end:
        break
  print(least[end-1])