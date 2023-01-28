import heapq

N=int(input())
mat=list(map(int, input().split()))
heapq.heapify(mat)
for i in range(N-1):
  mat2=list(map(int, input().split()))
  for j in range(N):
    heapq.heappush(mat, mat2.pop())
    heapq.heappop(mat)

print(heapq.heappop(mat))