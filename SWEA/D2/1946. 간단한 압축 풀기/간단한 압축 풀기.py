T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    ck=[]
    for i in range(N):
        Ci, Ki=input().split()
        ck+=[Ci]*int(Ki)
    idx=0
    print(f'#{test_case}')
    while idx<len(ck):
        print(*ck[idx:idx+10], sep='')
        idx+=10