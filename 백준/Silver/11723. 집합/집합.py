import sys
input=sys.stdin.readline

M=int(input())
S=set()
for i in range(M):
  command, *x=input().split()
  if command=='add':
    if int(x[0]) not in S:
      S.add(int(x[0]))
  elif command=='remove':
    if int(x[0]) in S:
      S.remove(int(x[0]))
  elif command=='check':
    if int(x[0]) in S:
      print(1)
    else:
      print(0)
  elif command=='toggle':
    if int(x[0]) in S:
      S.remove(int(x[0]))
    else:
      S.add(int(x[0]))
  elif command=='all':
    S=set(s for s in range(1, 21))
  else:
    S=set()