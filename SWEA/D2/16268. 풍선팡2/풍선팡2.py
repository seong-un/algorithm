T = int(input())
for test_case in range(1, T + 1):
    N, M=map(int, input().split())
    pollen=[]
    for n in range(N):
        pollen.append(list(map(int, input().split())))
    max_pollen=[]
    sum_pollen=0
    for i in range(N):
        for j in range(M):
            sum_pollen+=pollen[i][j]
            if i!=0:
                sum_pollen+=pollen[i-1][j]
            if i!=N-1:
                sum_pollen+=pollen[i+1][j]
            if j!=0:
                sum_pollen+=pollen[i][j-1]
            if j!=M-1:
                sum_pollen+=pollen[i][j+1]
            max_pollen.append(sum_pollen)
            sum_pollen=0
    print(f'#{test_case} {max(max_pollen)}')