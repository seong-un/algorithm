import heapq
import sys
input = sys.stdin.readline

N = int(input())
heap = []
list = []

for i in range(N):
    command = int(input())
    if command != 0:
        list.append(command)
        heapq.heappush(heap, abs(command))
    else:
        try:
            idx_pop = heapq.heappop(heap)
            if -idx_pop in list:
                list.remove(-idx_pop)
                print(-idx_pop)
            else:
                list.remove(idx_pop)
                print(idx_pop)
        except:
            print(0)