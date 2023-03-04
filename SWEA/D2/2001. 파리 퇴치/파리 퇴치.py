T=int(input())
for test_case in range(1, T+1):
    N, M=map(int, input().split())
    fly=[0]*N
    for i in range(N):
        fly[i]=list(map(int, input().split()))
  
    result=[]
    for i in range(N-M+1):
        for j in range(N-M+1):
            cnt=0
            for k in range(M):
                cnt+=sum(fly[i+k][j:j+M])
            result.append(cnt)
    print(f'#{test_case} {max(result)}')