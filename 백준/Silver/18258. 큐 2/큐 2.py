import sys
input=sys.stdin.readline
from collections import deque

N=int(input())
que=deque()
for i in range(N):
  command=list(input().split())
  if command[0]=='push':
    que.append(command[1])
  elif command[0]=='pop':
    if que:
      print(que.popleft())
    else:
      print(-1)
  elif command[0]=='size':
    print(len(que))
  elif command[0]=='empty':
    if que:
      print(0)
    else:
      print(1)
  elif command[0]=='front':
    if que:
      print(que[0])
    else:
      print(-1)
  else:
    if que:
      print(que[-1])
    else:
      print(-1)
