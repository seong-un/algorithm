import sys
input=sys.stdin.readline

N, K=map(int, input().split())
climate=list(map(int, input().split()))
list_climate=[sum(climate[:K])]+[0]*(N-K)
for i in range(N-K):
  list_climate[i+1]=list_climate[i]+climate[K+i]-climate[i]
print(max(list_climate))