from collections import deque

N = int(input())
G = [list(map(int, input().split())) for i in range(N)]
result = [[0] * N for i in range(N)]

for i in range(N):
    for j in range(N):
        queue = deque()
        queue.append(i)
        visited = []
        for_break = False
        while queue:
            a = queue.popleft()
            for idx, k in enumerate(G[a]):
                if k and (a, idx) not in visited:
                    queue.append(idx)
                    visited.append((a, idx))
                    if idx == j:
                        result[i][j] = 1
                        for_break = True
                        break
            if for_break:
                break

for i in result:
    print(*i)