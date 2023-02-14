T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    value=list(map(int, input().split()))
    result=0
    mx=value[-1]
    for i in range(N-1, -1, -1):
        if value[i]>mx:
            mx=value[i]
        else:
            result+=mx-value[i]
    print(f'#{test_case} {result}')