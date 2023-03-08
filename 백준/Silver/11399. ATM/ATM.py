N=int(input())
Pi=list(map(int, input().split()))
Pi.sort()
result=0
for i in range(N):
  result+=Pi[i]*N
  N-=1
print(result)