T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    sequence=list(input().split('0'))
    max_one=0
    for i in sequence:
        if max_one<len(i):
            max_one=len(i)
    print(f'#{test_case} {max_one}')