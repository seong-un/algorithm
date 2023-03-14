import sys
from collections import deque

input = sys.stdin.readline


N, M, K = map(int, input().split())
maze = [[] for i in range(N)]
for i in range(N):
    maze[i] = input().rstrip()

queue = deque()
queue.append((0, 0, 0))
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
visited = [[[0] * M for i in range(N)] for j in range(K + 1)]
visited[0][0][0] = 1
s = False
while queue:
    a = queue.popleft()
    x, y = a[0], a[1]
    for i in range(4):
        power = a[2]
        nx = x + dx[i]
        ny = y + dy[i]

        if nx < 0 or ny < 0 or nx > N - 1 or ny > M - 1:
            continue

        if visited[power][nx][ny]:
            continue

        if maze[nx][ny] == '1':
            if a[2] == K:
                continue
            else:
                power += 1

        if visited[power][nx][ny]:
            continue

        visited[power][nx][ny] = visited[a[2]][x][y] + 1
        queue.append((nx, ny, power))

        if nx == N - 1 and ny == M - 1:
            print(visited[power][N - 1][M - 1])
            s = True
            break
        
    if s:
        break
if not s and (N!=1 and M!=1):
    print(-1)
elif N==1 and M==1:
    print(1)