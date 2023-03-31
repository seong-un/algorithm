from itertools import combinations

T=int(input())
for test_case in range(1, T+1):
    N, L= map(int, input().split())
    kcal=[list(map(int, input().split())) for i in range(N)]
    burger=[]
    for i in range(1, N+1):
        for j in combinations(kcal, i):
            score = 0
            cal = 0
            for k in j:
                score+=k[0]
                cal+=k[1]
            if cal<=L:
                burger.append(score)
    print(f'#{test_case} {max(burger)}')