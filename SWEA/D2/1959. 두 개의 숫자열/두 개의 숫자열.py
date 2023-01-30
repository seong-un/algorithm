T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    N, M=map(int, input().split())
    A=list(map(int, input().split()))
    B=list(map(int, input().split()))
    L=[]
    if N>M:
        for i in range(N-M+1):
            sum=0
            for j in range(M):
                sum+=A[j+i]*B[j]
            L.append(sum)
        print(f"#{test_case} {max(L)}")
    else:
        for i in range(M-N+1):
            sum=0
            for j in range(N):
                sum+=A[j]*B[j+i]
            L.append(sum)
        print(f"#{test_case} {max(L)}")