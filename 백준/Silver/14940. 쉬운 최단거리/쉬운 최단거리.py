from collections import deque

n, m = map(int, input().split())
mapping = [[] for i in range(n)]
for i in range(n):
    mapping[i] = list(input().split())
    if '2' in mapping[i]:
        object = (i, mapping[i].index('2'))

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

queue = deque([object])
mapping[object[0]][object[1]] = 0
while queue:
    a, b = queue.popleft()
    for k in range(4):
        nx = a + dx[k]
        ny = b + dy[k]
        if nx < 0 or ny < 0 or nx > n - 1 or ny > m - 1:
            continue
        if mapping[nx][ny] == '1':
            mapping[nx][ny] = int(mapping[a][b]) + 1
            queue.append((nx, ny))
        if mapping[nx][ny] == '0':
            mapping[nx][ny] = 0

for i in range(n):
    for j in range(m):
        if mapping[i][j] == '1':
            mapping[i][j] = -1

for i in range(n):
    print(*mapping[i])