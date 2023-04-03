def dfs(i, j, K, cnt, mt):
    global depth
    if K<0:
        return
    for k in range(4):
        nx=i+dx[k]
        ny=j+dy[k]
        if nx<0 or ny<0 or nx>N-1 or ny>N-1 or (nx, ny) in visited:
            continue
        if mt[i][j]>mt[nx][ny]:
            visited.append((nx, ny))
            dfs(nx, ny, K, cnt+1, mt)
            visited.pop()
        elif 0<=mt[nx][ny]-mt[i][j]<K:
            visited.append((nx, ny))
            origin=mt[nx][ny]
            mt[nx][ny]=mt[i][j]-1
            dfs(nx, ny, 0, cnt+1, mt)
            mt[nx][ny]=origin
            visited.pop()
    depth=max(depth, cnt)
    return

dx=[-1, 1, 0, 0]
dy=[0, 0, -1, 1]

T=int(input())
for test_case in range(1, T+1):
    N, K= map(int, input().split())
    mt=[list(map(int, input().split())) for i in range(N)]
    summit=0
    for i in range(N):
        for j in range(N):
            summit=max(summit, mt[i][j])
    depth=0
    for i in range(N):
        for j in range(N):
            if mt[i][j]==summit:
                visited=[(i, j)]
                dfs(i, j, K, 1, mt)
    print(f'#{test_case} {depth}')