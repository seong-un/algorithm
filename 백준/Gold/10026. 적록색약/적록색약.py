from collections import deque
from copy import deepcopy

N = int(input())

paint = [list(input()) for i in range(N)]
copy_paint = deepcopy(paint)

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

origin = '0'
color = 0
for i in range(N):
    for j in range(N):
        if paint[i][j] == 0:
            continue
        color += 1
        origin = paint[i][j]
        queue = deque()
        queue.append((i, j))
        while queue:
            a, b = queue.popleft()
            for k in range(4):
                x = a + dx[k]
                y = b + dy[k]
                if x < 0 or y < 0 or x >= N or y >= N or paint[x][y] != origin:
                    continue
                paint[x][y] = 0
                queue.append((x, y))
print(color, end=" ")

origin = '0'
color = 0
for i in range(N):
    for j in range(N):
        if copy_paint[i][j] == 0:
            continue
        color += 1
        origin = copy_paint[i][j]
        queue = deque()
        queue.append((i, j))
        while queue:
            a, b = queue.popleft()
            for k in range(4):
                x = a + dx[k]
                y = b + dy[k]
                if x < 0 or y < 0 or x >= N or y >= N:
                    continue
                if origin in ['R', 'G']:
                    if copy_paint[x][y] not in ['R', 'G']:
                        continue
                else:
                    if copy_paint[x][y] != origin:
                        continue
                copy_paint[x][y] = 0
                queue.append((x, y))
print(color)