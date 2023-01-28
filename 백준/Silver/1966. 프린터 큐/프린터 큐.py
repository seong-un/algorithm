from collections import deque
tc=int(input())

for i in range(tc):
  n=0
  _, sv=map(int, input().split())
  D=deque(enumerate(map(int, input().split())))
  while True:
    if D[0][1]==max(D, key=lambda x:x[1])[1]:
      if D[0][0]!=sv:
        D.popleft()
        n+=1
      else:
        n+=1
        break
    else:D.append(D.popleft())
  print(n)