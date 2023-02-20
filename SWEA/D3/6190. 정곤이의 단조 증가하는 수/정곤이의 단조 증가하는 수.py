T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    Ai=list(map(int, input().split()))
    ascend=[]
    for i in range(N):
        for j in range(i+1, N):
            command=Ai[i]*Ai[j]
            lst=list(str(command))
            result=1
            L=len(lst)-1
            for k in range(L):
                if int(lst[k])>int(lst[k+1]):
                    result=0
            if result==1:
                ascend.append(command)
    if ascend:
        print(f'#{test_case} {max(ascend)}')
    else:
        print(f'#{test_case} -1')
