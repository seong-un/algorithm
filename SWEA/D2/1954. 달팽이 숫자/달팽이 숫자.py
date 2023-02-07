T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    snail = [[0] * N for i in range(N)]


    def snail_number(start, N):
        global cnt
        for i in range(N):
            snail[start][i + start] = cnt
            cnt += 1
        for i in range(1, N):
            snail[i + start][N - 1 + start] = cnt
            cnt += 1
        for i in range(1, N):
            snail[N - 1 + start][N - 1 - i + start] = cnt
            cnt += 1
        for i in range(1, N - 1):
            snail[N - 1 - i + start][start] = cnt
            cnt += 1
        if N < 2:
            return snail
        return snail_number(start + 1, N - 2)


    cnt = 1
    start = 0
    print(f'#{test_case}')
    for i in snail_number(start, N):
        print(*i)