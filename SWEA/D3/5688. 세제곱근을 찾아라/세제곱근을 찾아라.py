import math

T=int(input())
for test_case in range(1, T+1):
    N=int(input())
    if N==math.ceil(N**(1/3))**3:
        print(f'#{test_case} {math.ceil(N**(1/3))}')
    else:
        print(f'#{test_case} -1')