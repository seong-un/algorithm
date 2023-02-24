T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    home = [0] * N
    for i in range(N):
        home[i] = list(map(int, input().split()))
    sm = 0
    for i in home:
        sm += sum(i)
    k = 1
    while True:
        if 2 * k ** 2 - 2 * k + 1 < M * sm:
            k += 1
        else:
            k -= 1
            break
    while True:
        home_list = []
        for i in range(N):
            for j in range(N):
                homes = 0
                a = 0
                K = k
                while K > 0:
                    if i + a < N:
                        for b in range(K):
                            if j + b < N:
                                homes += home[i + a][j + b]
                        for b in range(1, K):
                            if j - b >= 0:
                                homes += home[i + a][j - b]
                    if a >= 1:
                        if i - a >= 0:
                            for b in range(K):
                                if j + b < N:
                                    homes += home[i - a][j + b]
                            for b in range(1, K):
                                if j - b >= 0:
                                    homes += home[i - a][j - b]
                    a += 1
                    K -= 1
                home_list.append(homes)
        if 2 * k ** 2 - 2 * k + 1 > max(home_list) * M:
            k -= 1
        else:
            break
    print(f'#{test_case} {max(home_list)}')
