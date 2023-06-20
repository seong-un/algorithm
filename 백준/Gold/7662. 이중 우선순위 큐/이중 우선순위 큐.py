import heapq
import sys
input = sys.stdin.readline

T = int(input())
for t in range(T):
    k = int(input())
    max_heap, min_heap = [], []
    visited = [False] * 1000001
    id = 1
    for K in range(k):
        string, n = input().split()
        n = int(n)
        if string == "I":
            heapq.heappush(max_heap, (-n, id))
            heapq.heappush(min_heap, (n, id))
            id += 1
        else:
            try:
                if n == -1:
                    while True:
                        a = heapq.heappop(min_heap)[1]
                        if visited[a]:
                            continue
                        else:
                            visited[a] = True
                            break
                else:
                    while True:
                        a = heapq.heappop(max_heap)[1]
                        if visited[a]:
                            continue
                        else:
                            visited[a] = True
                            break
            except:
                pass

    try:
        while True:
            value, a = heapq.heappop(max_heap)
            if visited[a]:
                continue
            else:
                print(-value, end=" ")
                break
        while True:
            value, a = heapq.heappop(min_heap)
            if visited[a]:
                continue
            else:
                print(value)
                break
    except:
        print("EMPTY")