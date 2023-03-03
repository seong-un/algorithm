P=int(input())
for _ in range(P):
  T, *height=map(int, input().split())
  sorting=[]
  cnt=0
  for h in height:
    for s in sorting:
      if s>h:
        cnt+=1
    sorting.append(h)
  print(T, cnt)