import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
  N, M=map(int, input().split())
  airplane=[0]*M
  for i in range(M):
    airplane[i]=list(map(int, input().split()))
  print(N-1)