T = int(input())
for t in range(T):
    M, N, x, y = map(int, input().split())
    if x == M:
        x = 0
    if y == N:
        y = 0
    l = 0
    while True:
        ans = M * l + x
        if ans <= 0:
            l += 1
            continue
        if ans % N == y:
            print(ans)
            break
        l += 1
        if ans > M * N:
            print(-1)
            break