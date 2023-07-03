import heapq

N = int(input())
rope = []
for i in range(N):
    heapq.heappush(rope, int(input()))

max_value = 0
for i in range(N, 0, -1):
    max_value = max(max_value, heapq.heappop(rope) * i)
print(max_value)