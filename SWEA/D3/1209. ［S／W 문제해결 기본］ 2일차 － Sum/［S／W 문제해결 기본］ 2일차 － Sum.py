for _ in range(10):
    test_case=int(input())
    L=[]
    for i in range(100):
        L.append(list(map(int, input().split())))
    maxi=[]
    for i in range(100):
        sum=0
        for j in range(100):
        	sum+=L[i][j]
        maxi.append(sum)
    for i in range(100):
        sum=0
        for j in range(100):
            sum+=L[j][i]
        maxi.append(sum)
    sum=0
    for i in range(100):
        sum+=L[i][i]
    maxi.append(sum)
    sum=0
    for i in range(100):
        sum+=L[99-i][i]
    maxi.append(sum)
    print(f'#{test_case} {max(maxi)}')