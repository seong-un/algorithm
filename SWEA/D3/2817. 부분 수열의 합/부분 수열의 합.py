from itertools import combinations

T=int(input())
for test_case in range(1, T+1):
    N, K=map(int, input().split())
    A=list(map(int, input().split()))

    cnt=0
    for i in range(1, N+1):
        for j in combinations(A, i):
            if sum(j)==K:
                cnt+=1

    print(f'#{test_case} {cnt}')