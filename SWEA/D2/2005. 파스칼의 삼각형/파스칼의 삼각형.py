T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    print(f'#{test_case}')
    print(1)
    start=[1,1]
    result=[1,1]
    for _ in range(N-1):
        print(*result)
        pascal=result[:]
        result=start[:]
        for i in range(len(pascal)-1):
            result.insert(i+1, pascal[i]+pascal[i+1])