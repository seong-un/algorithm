import heapq
import sys
input=sys.stdin.readline

N=int(input())

sort_heap=[]
for i in range(N):
  heapq.heappush(sort_heap, -int(input()))

for i in range(N):
  print(-heapq.heappop(sort_heap))