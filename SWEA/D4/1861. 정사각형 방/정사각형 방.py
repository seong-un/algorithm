T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    room = [[0] * N for i in range(N)]
    for i in range(N):
        room[i] = list(map(int, input().split()))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    cnt_list = []
    visited = []
    for i in range(N):
        for j in range(N):
            if room[i][j] not in visited:
                a, b = i, j
                cnt = 0
                while True:
                    moved = 0
                    cnt += 1
                    for k in range(4):
                        nx = a + dx[k]
                        ny = b + dy[k]
                        if nx < 0 or ny < 0 or nx > N - 1 or ny > N - 1:
                            continue
                        if room[nx][ny] == room[a][b] + 1:
                            a, b = nx, ny
                            visited.append(room[nx][ny])
                            moved = 1
                            break
                    if moved == 0:
                        cnt_list.append([room[i][j], cnt])
                        break
    mx = []
    for i in cnt_list:
        if i[1] == max(cnt_list, key=lambda x: x[1])[1]:
            mx.append(i)
    print(f'#{test_case}', *min(mx, key=lambda x: x[0]))
