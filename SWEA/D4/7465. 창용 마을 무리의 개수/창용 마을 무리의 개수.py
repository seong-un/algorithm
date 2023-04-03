from collections import deque

T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    relations = [[False] * N for i in range(N)]
    for i in range(M):
        a, b = map(int, input().split())
        relations[a - 1][b - 1] = True
        relations[b - 1][a - 1] = True
    visited = [False] * N
    cnt = 0
    while sum(visited) != N:
        for idx, i in enumerate(visited):
            if not i:
                idx = idx
                break

        queue = deque([idx])
        visited[idx]=True
        cnt += 1
        while queue:
            a = queue.popleft()
            for idx, i in enumerate(relations[a]):
                if i and not visited[idx]:
                    visited[idx] = True
                    queue.append(idx)

    print(f'#{test_case} {cnt}')
