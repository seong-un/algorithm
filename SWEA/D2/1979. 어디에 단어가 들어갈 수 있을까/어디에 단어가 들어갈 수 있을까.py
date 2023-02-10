T=int(input())
for test_case in range(1, T+1):
    N, K=map(int, input().split())
    puzzle=[0]*N
    for i in range(N):
        puzzle[i]=list(map(str, input().split()))
    cnt=0
    for i in puzzle:
        if i[:K]==['1']*K and i[K]=='0':
            cnt+=1
        if i[-K:]==['1']*K and i[-(K+1)]=='0':
            cnt+=1
        if '0'+'1'*K+'0' in ''.join(i):
            for j in range(N-K-1):
                if i[j:j+K+2]==['0']+['1']*K+['0']:
                    cnt+=1
    for i in list(zip(*puzzle)):
        if list(i)[:K]==['1']*K and list(i)[K]=='0':
            cnt+=1
        if list(i)[-K:]==['1']*K and list(i)[-(K+1)]=='0':
            cnt+=1
        if '0' + '1' * K + '0' in ''.join(i):
            for j in range(N - K - 1):
                if ''.join(i[j:j + K+2]) == '0' + '1' * K + '0':
                    cnt += 1
    print(f'#{test_case} {cnt}')