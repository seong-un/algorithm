T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    bus = []
    for i in range(N):
        bus.append(list(map(int, input().split())))
    P = int(input())
    C = []
    for i in range(P):
        C.append(int(input()))
    bus_stop = [0] * P
    for i in bus:
        for j in range(P):
            if i[0] <= C[j] <= i[1]:
                bus_stop[j] += 1
    print(f'#{test_case}', *bus_stop)