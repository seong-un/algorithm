import sys
input=sys.stdin.readline

N, M, B = map(int, input().split())
ground = [list(map(int, list(input().split()))) for i in range(N)]
mx = 0
mn = int(1e9)
for i in range(N):
    for j in range(M):
        mx = max(ground[i][j], mx)
        mn = min(ground[i][j], mn)
short_time = (int(1e9), 0)
for std in range(mn, mx + 1):
    time = 0
    inventory = B
    for_break = False
    for i in range(N):
        for j in range(M):
            if ground[i][j] > std:
                time += 2 * (ground[i][j] - std)
                inventory += ground[i][j] - std
            else:
                time += std - ground[i][j]
                inventory -= std - ground[i][j]
            if time > short_time[0]:
                for_break = True
                break
        if for_break:
            break
    if inventory >= 0:
        if time < short_time[0] or (time == short_time[0] and std > short_time[1]):
            short_time = (time, std)
print(*short_time)
