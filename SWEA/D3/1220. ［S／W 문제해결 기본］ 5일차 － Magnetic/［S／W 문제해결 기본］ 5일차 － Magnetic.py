for test_case in range(1, 11):
    N=int(input())
    table=[0]*N
    for i in range(N):
        table[i]=list(map(int, input().split()))
    table=list(zip(*table))
    deadlock=0
    for i in table:
        magnetic=False
        for j in i:
            if j==1 and not magnetic:
                magnetic=True
            if magnetic and j==2:
                deadlock+=1
                magnetic=False
    print(f'#{test_case} {deadlock}')