T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    time=[list(map(int, input().split())) for i in range(N)]
    time=sorted(time, key=lambda x:x[1])
    work=time[0]
    len_work=1
    for i in time:
        if work[1]>i[0]:
            continue
        work=i
        len_work+=1
    print(f'#{test_case} {len_work}')
