T = int(input())
for test_case in range(1, T + 1):
    t=int(input())
    score=list(map(int, input().split()))
    mod=[0]*101
    for i in range(101):
        for j in score:
            if i==j:
                mod[100-i]+=1
    print(f'#{t} {100-mod.index(max(mod))}')