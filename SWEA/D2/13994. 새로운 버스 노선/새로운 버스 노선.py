T = int(input())
for test_case in range(1, T + 1):
    N = int(input())
    bus = []
    for i in range(N):
        bus.append(list(map(int, input().split())))
    bus_stop = [0] * max(bus, key=lambda x: x[2])[2]
    for i in bus:
        if i[0] == 1:
            for j in range(i[1] - 1, i[2]):
                bus_stop[j] += 1
        elif i[0] == 2:
            for j in range(i[1] - 1, i[2], 2):
                bus_stop[j] += 1
            if i[2] % 2 != i[1] % 2:
                bus_stop[i[2] - 1] += 1
        else:
            if i[1] % 2 == 0:
                for j in range(i[1], i[2] + 1):
                    if j % 4 == 0:
                        bus_stop[j - 1] += 1
                if i[2] % 4 != 0:
                    bus_stop[i[2] - 1] += 1
                if i[1] % 4 == 2:
                    bus_stop[i[1] - 1] += 1
            elif i[1] % 2 == 1:
                for j in range(i[1], i[2] + 1):
                    if j % 3 == 0 and j % 10 != 0:
                        bus_stop[j - 1] += 1
                if i[1] % 3 != 0 or i[1] % 30 == 0:
                    bus_stop[i[1] - 1] += 1
                if i[2] % 3 != 0 or i[2] % 30 == 0:
                    bus_stop[i[2] - 1] += 1
    print(f'#{test_case} {max(bus_stop)}')