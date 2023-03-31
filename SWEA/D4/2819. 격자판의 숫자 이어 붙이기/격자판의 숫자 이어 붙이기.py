def dfs(num_len, i, j, number):
    if num_len == 7:
        set_number.add(number)
        return
    for k in range(4):
        nx = i + dx[k]
        ny = j + dy[k]
        if nx < 0 or ny < 0 or nx > 3 or ny > 3:
            continue

        dfs(num_len + 1, nx, ny, number + grid[nx][ny])


T = int(input())
for test_case in range(1, T + 1):
    grid = [list(input().split()) for i in range(4)]
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    set_number = set()
    for i in range(4):
        for j in range(4):
            # number=[]
            dfs(1, i, j, grid[i][j])

    print(f'#{test_case} {len(set_number)}')