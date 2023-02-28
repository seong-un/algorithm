for test_case in range(1, 11):
    N=int(input())
    table=[0]*N
    for i in range(N):
        table[i]=list(input().split())
    table=list(zip(*table))
    cnt=0
    for i in table:
        cnt+=''.join(i).replace('0', '').count('12')
    print(f'#{test_case} {cnt}')