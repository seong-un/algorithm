T = int(input())
for test_case in range(1, T + 1):
    N, M = map(int, input().split())
    data = [0] * N
    for i in range(N):
        data[i] = list(map(int, input().split()))
    cnt=0
    result=[]
    for i in range(N):
        for j in range(M):
            if data[i][j] == 1:
                a,b=i,j
                if a != N - 1 and data[a + 1][b] == 1:
                    while True:
                        if a != N - 1 and data[a + 1][b] == 1:
                            cnt+=1
                            a+=1
                        else:
                            cnt+=1
                            result.append(cnt)
                            cnt=0
                            break
                elif b!=M-1 and data[a][b+1]==1:
                    while True:
                        if b != M - 1 and data[a][b+1] == 1:
                            cnt+=1
                            b+=1
                        else:
                            cnt+=1
                            result.append(cnt)
                            cnt=0
                            break
    print(f'#{test_case} {max(result)}')