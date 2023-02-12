import sys
input=sys.stdin.readline

N=int(input())
point=[0]*N
for i in range(N):
  point[i]=list(map(int, input().split()))
point=sorted(point, key=lambda x:(x[1], x[0]))
for i in point:
  print(*i)