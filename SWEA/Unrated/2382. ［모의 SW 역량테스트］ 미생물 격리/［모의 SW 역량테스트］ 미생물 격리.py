import copy

T = int(input())
for test_case in range(1, T + 1):
    N, M, K = map(int, input().split())
    organism = [list(map(int, input().split())) for i in range(K)]
    area = [[0] * N for i in range(N)]
    for i in organism:
        area[i[0]][i[1]] = [i[2], i[3]]
    time=0
    while time<M:
        time+=1
        comb=set()
        area_copy=[[[] for i in range(N)] for i in range(N)]
        for i in range(N):
            for j in range(N):
                if area[i][j]==0:
                    continue
                if area[i][j][1] == 1:
                    area_copy[i - 1][j].append(area[i][j])
                    if i-1 == 0:
                        area_copy[i-1][j][0][0]=area_copy[i-1][j][0][0]//2
                        area_copy[i-1][j][0][1] = 2
                        continue
                    continue
                if area[i][j][1] == 2:
                    area_copy[i + 1][j].append(area[i][j])
                    if i+1 == N-1:
                        area_copy[i+1][j][0][0]=area_copy[i+1][j][0][0]//2
                        area_copy[i+1][j][0][1] = 1
                        continue
                    continue
                if area[i][j][1] == 3:
                    area_copy[i][j-1].append(area[i][j])
                    if j-1 == 0:
                        area_copy[i][j-1][0][0]=area_copy[i][j-1][0][0]//2
                        area_copy[i][j-1][0][1] = 4
                        continue
                    continue
                if area[i][j][1] == 4:
                    area_copy[i][j+1].append(area[i][j])
                    if j+1 == N-1:
                        area_copy[i][j+1][0][0]=area_copy[i][j+1][0][0]//2
                        area_copy[i][j+1][0][1] = 3
                        continue
                    continue
        for i in range(N):
            for j in range(N):
                if area_copy[i][j]==[]:
                    area[i][j]=0
                    continue
                sm=0
                for k in area_copy[i][j]:
                    sm+=k[0]
                area[i][j]=[sm, max(area_copy[i][j], key=lambda x:x[0])[1]]
    result=0
    for i in range(N):
        for j in range(N):
            if area[i][j]==0:
                continue
            result+=area[i][j][0]
    print(f'#{test_case} {result}')