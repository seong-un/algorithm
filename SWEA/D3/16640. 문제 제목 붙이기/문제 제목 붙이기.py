T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    title=[0]*N
    for t in range(N):
        title[t]=input()[0]
    s=0
    while chr(ord('A')+s) in title:
        s+=1
    print(f'#{test_case} {s}')