import sys
input=sys.stdin.readline

N, M=map(int, input().split())
upper=[list(input().split())]
for i in range(N-1):
  a=list(input().split())
  if upper[-1][1]!=a[1]:
    upper.append(a)
power=[0]*M
for i in range(M):
  power[i]=int(input())
idx=[0]*len(power)
for ix, i in enumerate(power):
  start=0
  end=len(upper)-1
  while start<=end:
    mid=(start+end)//2
    if int(upper[mid][1])<i:
      start=mid+1
      idx[ix]=mid+1
    elif int(upper[mid][1])>i:
      end=mid-1
    else:
      idx[ix]=mid
      break
for i in idx:
  print(upper[i][0])