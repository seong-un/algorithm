import sys
input = sys.stdin.readline

dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

N, M = map(int, input().split())
tetromino = [list(map(int, input().split())) for i in range(N)]

def dfs(x, y, visited):
    global max_total

    if len(visited) == 4:
        total = 0
        for i, j in visited:
            total += tetromino[i][j]
        return total

    for i in range(4):
        xx = x + dx[i]
        yy = y + dy[i]
        if xx < 0 or yy < 0 or xx >= N or yy >= M or (xx, yy) in visited:
            continue
        visited.append((xx, yy))
        max_total = max(max_total, dfs(xx, yy, visited))
        visited.pop()

    return max_total

max_total = 0
for i in range(N):
    for j in range(M):
        max_total = max(max_total, dfs(i, j, [(i, j)]))

for i in range(N):
    for j in range(M):
        for k in range(4):
            current = tetromino[i][j]
            try:
                if k != 0:
                    current += tetromino[i + dx[0]][j + dy[0]]
                if k != 1:
                    if i + dx[1] < 0:
                        raise ValueError
                    current += tetromino[i + dx[1]][j + dy[1]]
                if k != 2:
                    current += tetromino[i + dx[2]][j + dy[2]]
                if k != 3:
                    if j + dy[3] < 0:
                        raise ValueError
                    current += tetromino[i + dx[3]][j + dy[3]]
            except:
                continue
            max_total = max(max_total, current)

print(max_total)