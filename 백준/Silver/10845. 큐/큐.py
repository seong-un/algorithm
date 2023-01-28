from collections import deque
import sys
input = sys.stdin.readline

N = int(input())
D=deque()
for i in range(1,N+1):
  st=list(map(str,input().split()))
  if st[0]=="push":
    D.append(st[1])
  if st[0]=="pop":
    if not D:
      print(-1)
    else:
      print(D[0])
      D.popleft()
  if st[0]=="size":
    print(len(D))
  if st[0]=="empty":
    print(int(not D))
  if st[0]=="front":
    if not D:
      print(-1)
    else:print(D[0])
  if st[0]=="back":
    if not D:
      print(-1)
    else:print(D[-1])