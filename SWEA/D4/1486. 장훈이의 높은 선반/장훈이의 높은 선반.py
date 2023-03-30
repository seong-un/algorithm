from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
    N, B=map(int, input().split())
    H=list(map(int, input().split()))
    result=999999999
    for i in range(1, N+1):
        for j in combinations(H, i):
            s=sum(j)
            if s>=B:
                result=min(result, s-B)
    print(f'#{test_case} {result}')