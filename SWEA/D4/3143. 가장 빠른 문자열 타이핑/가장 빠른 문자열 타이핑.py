T=int(input())
for test_case in range(1, T+1):
    A, B=input().split()
    print(f'#{test_case} {len(A)-A.count(B)*(len(B)-1)}')