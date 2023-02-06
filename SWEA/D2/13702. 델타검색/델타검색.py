for test_case in range(1, 11):
    N=int(input())
    array=[]
    for i in range(N):
        array.append(list(map(int, input().split())))
    list_sum=0
    for i in range(N):
        for j in range(N):
            if i!=0:
                list_sum+=abs(array[i][j]-array[i-1][j])
            if i!=N-1:
                list_sum+=abs(array[i][j]-array[i+1][j])
            if j!=0:
                list_sum+=abs(array[i][j]-array[i][j-1])
            if j!=N-1:
                list_sum+=abs(array[i][j]-array[i][j+1])
    print(f'#{test_case} {list_sum}')