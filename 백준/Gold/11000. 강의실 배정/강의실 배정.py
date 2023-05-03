import heapq
N = int(input())
lst = [list(map(int,input().split())) for _ in range(N)]

lst.sort(key= lambda x: (x[0]))
heap = [lst[0][1]]

for s, e in lst[1:]:
  
  if heap[0] <= s:
    heapq.heappop(heap)

  heapq.heappush(heap, e)
    
print(len(heap))