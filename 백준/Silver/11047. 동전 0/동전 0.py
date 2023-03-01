N, K=map(int, input().split())
Ai=[0]*N
for i in range(N):
  Ai[i]=int(input())
coin=0
Ai.reverse()
for i in Ai:
  coin+=K//i
  K=K-K//i*i
print(coin)