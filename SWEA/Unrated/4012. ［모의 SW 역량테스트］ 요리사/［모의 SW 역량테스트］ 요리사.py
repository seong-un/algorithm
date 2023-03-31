from itertools import combinations

T = int(input())
for test_case in range(1, T + 1):
    N=int(input())
    S=[list(map(int, input().split())) for i in range(N)]
    food=set([i for i in range(N)])
    Sab=float('inf')
    for i in combinations([i for i in range(N)], int(N/2)):
        A=set(i)
        B=food-A
        Sa=0
        Sb=0
        for j in combinations(A, 2):
            Sa+=S[j[0]][j[1]]+S[j[1]][j[0]]
        for j in combinations(B, 2):
            Sb+=S[j[0]][j[1]]+S[j[1]][j[0]]
        Sab=min(Sab, abs(Sa-Sb))
    print(f'#{test_case} {Sab}')